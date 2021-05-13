n,q=map(int, input().split())
s=input()
lr = [list(map(int,input().split())) for _ in range(q)]

cum = [0]*(n+1)
pre = s[0]
cnt=0
for i in range(1,n):
    now = s[i]
    if pre=="A" and now=="C":
        cnt+=1
    cum[i+1] = cnt
    pre = now
for l,r in lr:
    print(cum[r]-cum[l])