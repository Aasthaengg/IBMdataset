a, b = map(int, input().split())
if abs(a - b) % 2 == 1:
    print('IMPOSSIBLE')
else:
    dif = abs(a - b) // 2
    if a < b:
        print(a + dif)
    else:
        print(b + dif)