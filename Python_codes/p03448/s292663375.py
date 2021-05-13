import itertools

a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = x//50

p = 0

list_s = list(range(a+1))
list_t = list(range(b+1))
list_u = list(range(c+1))

for s,t,u in itertools.product(list_s,list_t,list_u):
    m = 10*s + 2*t + u
    if m == y:
        p += 1

print(p)