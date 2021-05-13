N, A, B = map(int, input().split())
val = [int(i) for i in input().split()]

def combi(n, m):
    from math import factorial
    return factorial(n) // (factorial(m) * factorial(n-m))

val.sort(reverse=True)
ave = sum(val[:A])/A

l = val.index(val[A-1])
x = val.count(val[A-1])
ct = 0

if val[0] == val[A-1]:
    for i in range(A, x+1):
        if i > B:
            break
        else:
            ct += combi(x, i)
else:
    ct = combi(x, A-l)
print(ave)
print(ct)
