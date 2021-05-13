N, x = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

current = x
result = 0

for i in range(N):
    if  current >= a[i]:
        current -= a[i]
        result += 1

if result == N and current > 0:
    result -= 1

print(result)