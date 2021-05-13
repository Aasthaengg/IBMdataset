n = int(input())

print(0)
s = str(input())
if s == 'Vacant':
    exit()
s0 = s

print(n-1)
s = str(input())
if s == 'Vacant':
    exit()

def is_ok(x):
    print(x)
    s = str(input())
    if s == 'Vacant':
        exit()
    if x%2 == 1:
        if s != s0:
            return False
        else:
            return True
    else:
        if s == s0:
            return False
        else:
            return True


l = 0
r = n-1
while l+1 < r:
    c = (l+r)//2
    if is_ok(c):
        r = c
    else:
        l = c
