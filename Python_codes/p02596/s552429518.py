K = int(input())
INF = 10**18

a = [INF] * (K+1)
a[0] = 0

for n in range(1, K+1):
    a[n] = (10 * a[n-1] + 7) % K
    if a[n] == 0:
        print(n)
        break
else:
    print(-1)
