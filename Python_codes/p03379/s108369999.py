n=int(input())
N=list(map(int,input().split()))
N2 = sorted(N)
#print(N2)
nl=N2[int(n/2)-1]
nr=N2[int(n/2)]
for i in N:
  if i<=nl:
    print(nr)
  else:
    print(nl)