n = int(input())
k = int(input())

ans = 1
while n > 0:
    a = ans * 2;
    b = ans + k
    ans = min(a, b)
    n -= 1

print(ans)
