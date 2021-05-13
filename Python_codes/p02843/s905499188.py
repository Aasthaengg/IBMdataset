X = int(input())
c, r = 0, X % 100
for d in range(5, 0, -1):
    c += r // d
    r = r % d
if c > X // 100:
    print(0)
else:
    print(1)