n, a, b = map(int, input().split())
if a > b:
    ans = 0
elif n == 1 and a == b:
    ans = 1
elif n == 1:
    ans = 0
elif a == b:
    ans = 1
else:
    maxVal = a * 1 + b * (n-1)
    minVal = a * (n-1) + b * 1
    ans = maxVal - minVal + 1
print(ans)
