import sys
sys.setrecursionlimit(200000)
N,K = map(int,input().split())
A = list(map(int,input().split()))
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
g = A[0]
for i in range(1,N):
    g = gcd(g,A[i])
if K > max(A):
    print("IMPOSSIBLE")
    exit()
if K % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")