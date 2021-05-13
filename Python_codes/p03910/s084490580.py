from math import sqrt
n=int(input())
d=min(-(-int(sqrt(8*n+1))//2),n)
l=list(range(1,d+1))
remain=(d*(d+1))//2-n

while remain>=l[-1]:
    remain-=l[-1]
    l.pop()
print(*list(set(l)-set([remain])),sep="\n")