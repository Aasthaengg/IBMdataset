from collections import deque

N=int(input())
S=input()

d={'I':1, 'D':-1}
l=[0]*(N+1)

for x in range(1,N+1):
  l[x]=l[x-1]+d[S[x-1]]

print(max(l))