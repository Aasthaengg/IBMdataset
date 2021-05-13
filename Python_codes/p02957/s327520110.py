a, b = map(int, input().split())
s = a + b
if s % 2 == 0:
    print(s//2)
else:
    print("IMPOSSIBLE")
