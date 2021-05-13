n,k=map(int, input().split( ))
w = []
for _ in range(n):
    w.append(int(input()))
mx=sum(w)
mn=max(w)##mx//k<max(w)が抜けてる
mid = (mx+mn)//2
w.append(1000000000000000)

while mn < mid:#このループ条件が不自然みたいだが
    cnt = 1
    sm = 0
    for i in range(n):#ここがwhileだったのを修正して減らした
        if sm <= mid-w[i]:
            sm +=  w[i]
        else:
            cnt+=1
            sm = w[i]

    if cnt>k:
        mn = mid
        mid = (mid+mx)//2
    else:
        mx = mid
        mid = (mid+mn)//2
#最終的な実行可能解が不明、結局最後mn,mid,mx全部チェックしてる
ans=[]
for a in [mn,mid,mx]:
    cnt = 1
    sm = 0
    for i in range(n):
        if sm <= a - w[i]:
            sm +=  w[i]
        else:
            cnt+=1
            sm = w[i]

    if cnt<=k:
        ans.append(a)
    else:
        pass

print(min(ans))
#最終的な実行可能解は(直前までmidだった)mx

