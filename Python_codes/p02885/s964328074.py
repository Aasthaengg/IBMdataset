a,b = map(int, input().split())

ans = a - b - b

if ans > 0:
    print(ans)
else:
    print(0)