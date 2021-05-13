N = int(input())
ans = 0

for i in range(1,N):
    if i >= (N - i) / i:
        break
    if (N - i) % i == 0:
        a = (N - i) // i
        ans += a

print(ans)