a, b = map(int, input().split())

if int(a / 0.08 * 0.1) == b:
    print(round(a / 0.08 + 0.0001))
elif int(b / 0.1 * 0.08) == a:
    print(round(b / 0.1 + 0.0001))
else:
    print(-1)
