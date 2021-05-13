N,K=map(int, input().split())
*A,=map(int, input().split())

X=0
for i in range(40,-1,-1):
    b = 1<<i
    if X|b>K:continue
    c=0
    for a in A:
        if a&b: c+=1
    if c <= N//2: X|=b

ans=0
for a in A:
    ans += a^X
print(ans)
