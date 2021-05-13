#「探索候補スタック」「探索済みリスト」「現在地点」の３点セットでとらえる
n,q=map(int,input().split())
mat=[set() for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    mat[a-1].add(b-1)
    mat[b-1].add(a-1) # プラスした要素
count=[0]*n
for _ in range(q):
    p,score=map(int,input().split())
    count[p-1]+=score

stack=[[0,0,-1]]
while stack:
    # print(stack)
    num,cnt,pr=stack.pop()
    count[num]+=cnt
    for k in mat[num]:
        if k==pr:
            continue
        stack.append([k,count[num],num])
print(*count)