N = int(input())

ans = 0

for i in range(1, N+1):
    ans += i
    if ans >= N:
        break

for j in range(1, i+1):
    if ans - N == j:
        continue
    print(j)