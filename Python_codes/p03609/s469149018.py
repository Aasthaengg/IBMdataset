x, t = (int(x) for x in input().split())

if x > t:
    ans = x-t
else:
    ans = 0
print(ans)