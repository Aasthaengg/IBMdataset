N, M, C = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
ans = 0
for i in range(N):
    A = [int(n) for n in input().split()]
    t = 0
    for a,b in zip(A, B):
        t += a*b
    if t+C > 0:
        ans += 1
print(ans)
