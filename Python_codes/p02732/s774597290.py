import collections
N=int(input())
A=list(map(int,input().split()))
c = collections.Counter(A)
x = 0
#print(c)
for i in c.values():
    x += i*(i-1)//2
#print(x)
for i in range(N):
    print(x-c[A[i]]+1)
