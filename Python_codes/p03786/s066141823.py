n = int(input())
a = list(map(int,input().split()))
a.sort()

l = 0
r = n - 1

def hantei(c):
    a1 = a[:c] + a[c+1:]
    tmp = a[c]
    flag = True
    for i in a1:
        if tmp * 2 >= i:
            tmp += i
        else:
            flag = False
            break
    return flag


while r - l > 1:
    c = int((l + r)//2)
    if hantei(c):
        r = c
    else:
        l = c

if hantei(l):
    print(n - l)
else:
    print(n - l - 1)
