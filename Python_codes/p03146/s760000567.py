n=int(input())
from collections import defaultdict
d=defaultdict(int)
def find(n,i):
    if d[n]!=0:
        return i
    d[n]=i
    if n%2==0:
        return find(n//2,i+1)
    else:
        return find(3*n +1 ,i+1)

print(find(n,1))
