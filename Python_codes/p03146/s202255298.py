s = int(input())

def f(n):
    if n%2 == 0:
        return n // 2
    else:
        return 3*n + 1

a = [s]
for i in range(1, 1000001):
    if a[i-1] in a[:i-1]:
        print(i)
        break
    else:
        a.append(f(a[i-1]))