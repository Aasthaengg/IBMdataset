s = int(input())

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

a = [s]
i = 2
while True:
    x = f(a[i-2])
    if x in a:
        print(i)
        break
    a.append(x)
    i += 1