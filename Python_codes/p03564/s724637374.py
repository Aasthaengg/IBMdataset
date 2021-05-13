N=int(input())
K=int(input())
ans=float('inf')
for i in range(2**N):
    bi=list(format(i,'b').zfill(N))
    now=1
    for b in bi:
        if b=='0':
            now*=2
        else:
            now+=K
    if now<ans:
        ans=now
print(ans)