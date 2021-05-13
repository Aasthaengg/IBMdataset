n = int(input())
A = []
for i in range(1, n // 2 + 1):
    a = str(i)
    b = str(n - i)
    t = 0
    for j in a:
        t += int(j)
    for k in b:
        t += int(k)
    A.append(t)
print(min(A))