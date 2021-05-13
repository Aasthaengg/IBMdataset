num = input().split()
a, b =int(num[0]), int(num[1])

ans = sorted([a+b, a-b, a*b])

print(ans[-1])