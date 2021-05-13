n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
e = []
def kome(p):
    c = 0
    for i in range(n):
        c = c + (abs(a[i] - b[i]) ** p)
        e.append(abs(a[i] - b[i]))
    d = c ** (1 / p)
    return d
    
print(kome(1))
print(kome(2))
print(kome(3))
print(float(max(e)))
