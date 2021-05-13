import math
N, K = map(int, input().split())
ans = 0
for n in range(1, N+1):
    if n >= K:
        ans += 1/N
    else:
        ans += (1/N)*(1/2)**(math.ceil(math.log(K/n, 2)))
print(ans)