n = int(input())
P = list(map(int,input().split()))
prev = False
ans = 0
for i,p in enumerate(P):
    if i+1 == p:
        if prev:
            prev = False
        else:
            ans+=1
            prev=True
    else:prev=False
print(ans)
