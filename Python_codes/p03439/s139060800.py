n = int(input())

def q(x):
    print(x)
    s = str(input())
    if s == 'Vacant':
        exit()
    else:
        return s

y = q(0)
q(n-1)

def ok(x):
    if x%2 == 0:
        if y == q(x):
            return False
        else:
            return True
    else:
        if y != q(x):
            return False
        else:
            return True

l = 0
r = n-1
while l+1 < r:
    c =(l+r)//2
    if ok(c):
        r = c
    else:
        l = c
print(r)