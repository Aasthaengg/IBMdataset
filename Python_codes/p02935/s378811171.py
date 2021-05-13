N=int(input())
*v,=sorted(map(int,input().split()))

from bisect import insort
c=1
while c<N:
    insort(v,(v.pop(0) + v.pop(0)) / 2)
    c+=1
print(*v)