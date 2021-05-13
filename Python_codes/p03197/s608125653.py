n = int(input())
ans = 'second'

for _ in range(n):
    a = int(input())
    if a % 2 == 1:
        ans = 'first'

print(ans)
