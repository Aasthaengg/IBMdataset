s = int(input())

def f(n):
    if n%2==0:
        return int(n/2)
    else:
        return int(3*n+1)

a=[s]
for i in range(10000000):
    a_last = f(a[i])
    if a_last in a:
        print(i+2)
        break
    a.append(a_last)
