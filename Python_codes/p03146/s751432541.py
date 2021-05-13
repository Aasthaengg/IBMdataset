s = int(input())

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

a = [s]
i = 1
while True:
    s = f(s)
    i += 1
    if s in a:
        break
    a += [s]
print(i)