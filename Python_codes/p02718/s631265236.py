def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

n,m=sep()
ar=lis()
ar.sort(reverse=True)
k=ar[m-1]
if k>=((sum(ar)/(4*m))):
    print("Yes")
else:
    print("No")
