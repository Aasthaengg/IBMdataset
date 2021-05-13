a, b, x = map(int, input().split())
a += (x - a % x) if a % x != 0 else 0
answ = (b - a) // x if a % x != 0 else (b - a) // x + 1
print(answ)
