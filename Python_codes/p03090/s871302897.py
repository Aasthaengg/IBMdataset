import sys
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
n=int(input())
tmp=(n+1)//2*(n-2)
# print(tmp)
if n%2==0:
    print(n*(n-2)//2)
else:
    print(((n-1)*(n-3))//2+n-1)
for i in range(n):
    for j in range(i+1,n):
        if (i+1)+(j+1)!=n+(n+1)%2:
            print(i+1,j+1)