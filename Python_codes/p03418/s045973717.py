n, k = map(int, input().split())

if k == 0:
    print(n**2)
    exit()

answer = 0
for i in range(k + 1, n + 1):
    q = n // i; r = n % i
    answer += (i - k) * q
    if r >= k:
        answer += r - k + 1

print(answer)
