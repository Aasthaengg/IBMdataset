def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]

n,m = inL()
h = inL()
ab = inNL(m)

l = [1]*n
for a,b in ab:
    if h[a-1]>h[b-1]:
        l[b-1] = 0
    elif h[a-1]==h[b-1]:
        l[a-1]=l[b-1]=0
    else:
        l[a-1] = 0
#print(l)
print(l.count(1))
