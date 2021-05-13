n = int(input())
a = list(map(int, input().split()))
x = 1
for i in a:
    x *= (2 - (i % 2))
ans = pow(3, n) - x
print(ans)