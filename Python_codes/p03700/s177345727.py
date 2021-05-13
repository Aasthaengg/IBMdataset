N,A,B=map(int,input().split())
h=[]
hmax=0
for i in range(N):
    i=int(input())
    hmax=max(hmax,i)
    h.append(i)

def check(t):
    l=[]
    for i in h:
        i-=t*B
        if i > 0:
            l.append(i)
    if len(l) != 0:
        while t>=0:
            i=l.pop()
            t-=-(-i//(A-B))
            if (len(l)==0) and (t>=0):
                return True
        return False
    else:
        return True

min=0
max=hmax
while max != min + 1:
    j=(max-min)//2+min
    if check(j) == True:
        max = j
    else:
        min = j
print(max)
