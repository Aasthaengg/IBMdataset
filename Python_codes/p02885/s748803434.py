a, b = map(int, input().split())
ans = a - b - b
if ans < 0:
    print('0')
else:
    print(ans)