N = int(input())
rem = []

for i in range(1, N):
    if i * i > N:
        break
    elif i * i == N:
        rem.append(i)
    elif N % i == 0:
        rem.extend([i, N // i])

ans = 0
for r in rem:
    if (r - 1) > N // r:
        ans += r - 1
print(ans)