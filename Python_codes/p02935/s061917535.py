N=int(input())
v=[int(x) for x in input().split()]
v.sort()
S=v[0]/2**(N-1)
for i in range(1,N):
  S=S+(v[i]/2**(N-i))
print(S)