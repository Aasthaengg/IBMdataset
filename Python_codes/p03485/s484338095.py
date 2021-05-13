a, b = map(int, input().split())
c = (a + b) / 2
n = str(c)
if n[len(n) - 1] == '0':
    print(int(c))
else:
    print(int(c) + 1)