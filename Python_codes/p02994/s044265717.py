N, L = map(int, input().split())
ans = 0

if L>0:
    for i in range(N-1):
        ans += L+i+1
    print(ans)
    exit()

if L<=0 and N+L-1 <= 0:
    for i in range(N-1):
        ans += L+i
    print(ans)
    exit()

for i in range(N):
    ans += L+i
print(ans)


