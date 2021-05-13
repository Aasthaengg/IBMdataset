N = int(input())

ans = 0
for n in range(N+1):
    if n*n <= N: ans = n*n
    else: break
print(ans)