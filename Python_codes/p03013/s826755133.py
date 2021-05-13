N, M = map(int, (input().split()))
n = [0] * (N+1)
for i in range(M):
    n[int(input())] = True
f = [1]
for i in range(1, N+1):
    if n[i]:
        f.append(0)
    elif i == 1:
        f.append(f[0])
    else:
        f.append((f[i-1]+f[i-2])%(10**9+7))
print(f[N])
