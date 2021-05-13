n, a, b = map(int, input().split())
ans = (b*n-b+a) - (a*n-a+b) + 1

if a > b:
    ans = 0
elif a != b and n == 1:
    ans = 0

print(ans)