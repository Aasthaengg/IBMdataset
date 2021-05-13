s = int(input())

def f(n):
    if n%2 == 0:
        return n // 2
    else:
        return 3*n + 1

a = []
for i in range(1, 1000001):
    if i == 1:
        a.append(s)
    else:
        n = a[i-2]
        a.append(f(n))

b = []
for i, num in enumerate(a):
    if num in b:
        print(i+1)
        break
    b.append(num)