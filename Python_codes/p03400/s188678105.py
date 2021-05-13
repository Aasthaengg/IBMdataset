n = int(input())
d, x = map(int, input().split())
A = list()
for a in range(n):
    A.append(int(input()))

ans = 0

for a in range(n):
    day = 1
    while day <= d:
        ans += 1
        day += A[a]

print(ans+x)
