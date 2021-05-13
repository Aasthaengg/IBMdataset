import bisect
import sys
input = lambda: sys.stdin.readline().rstrip()

n=int(input())
s= list(input())
q=[]
qq=int(input())
for i in range(qq):
    q.append(list(input().split()))

# アルファベットごとに出現位置を記録
x=[[] for i in range(26)]
for i,j in enumerate(s):
    x[ord(j)-97].append(i)

# 終点対策
for i in range(26):
    x[i].append(5*10**5)


for i,j,k in q:
    if int(i)==1:
        if s[int(j)-1]!=k:
            v=s[int(j)-1]
            s[int(j)-1]=k
            # 変更前の要素を削除
            index=bisect.bisect_right(x[ord(v)-97], int(j)-1) - 1
            x[ord(v)-97].pop(index)
            # 変更後の要素を加える
            bisect.insort_right(x[ord(k)-97],int(j)-1)
    else:
        cnt=0
        j=int(j)-1
        k=int(k)-1
        for l in range(26):
            index=bisect.bisect_left(x[l],j)
            if x[l][index]<=k:
                cnt+=1


        print(cnt)