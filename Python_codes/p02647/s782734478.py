def right(a,n):
    sw = [0]*(n+1)
    for x,y in enumerate(a):
        x_min = max(0,x-y)
        x_max = min(n,x+y+1)
        sw[x_min] += 1
        sw[x_max] -= 1
    s = 0
    for i in range(n):
        s += sw[i]
        a[i] = s
    return a

n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(min(k,50)):
    a = right(a,n)
a = [str(n) for n in a]
print(" ".join(a))