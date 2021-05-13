n,m = map(int,input().split())

def f(m):
    d = []
    r = int(m**0.5)
    for i in range(1,r+1):
        if m % i == 0:
            d.append(i)
            d.append(m//i)
    d.sort(reverse = 1)
    return d

d = f(m)
for x in d:
    p = m//x
    #print(x,p)
    #if n <= p and p % n != 0:
    if n <= p:
        print(x)
        exit() 