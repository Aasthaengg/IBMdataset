n = int(input())
if n == 1:
    print(1)
else:
    l = [2, 1]
    for _ in range(n - 1):
        l.append(l[-2] + l[-1])
    print(l[-1])