A, B = map(int, input().split())
c = 0
for i in range(A, B + 1):
    n = str(i)
    r = str(i)[::-1]
    if n == r:
        c += 1
print(c)