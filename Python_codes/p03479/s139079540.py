x, y = [int(s) for s in input().split()]
ans = 0
temp = x
while temp <= y:
    ans += 1
    temp *= 2
print(ans)