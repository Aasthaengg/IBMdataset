a, b = map(int, input().split())
if (b == 1):
    ans = 0
elif (a >= b):
    ans = 1
else:
    result = a*2 - 1
    ans = 2
    while result < b:
        result += a-1
        ans += 1
print(ans)