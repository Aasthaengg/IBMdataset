a, b = map(int, input().split())

k = (a+b)/2

if abs(a-k) == abs(b-k) and (a+b) % 2 == 0:
    print(int(k))
else:
    print("IMPOSSIBLE")