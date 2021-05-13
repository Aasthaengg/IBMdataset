def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

x, y = MI()
ans = 0

if abs(x) == abs(y):
    ans = int(x * y < 0)

elif abs(x) < abs(y):
    ans = abs(abs(y) - abs(x)) + int(x < 0) + int(y < 0)

else:
    ans = abs(abs(y) - abs(x)) + int(x * y <= 0) + int(x > 0 and y > 0) * 2
    if x < 0 and y == 0:
        ans -= 1

print(ans)