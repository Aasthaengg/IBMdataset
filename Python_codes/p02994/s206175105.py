N,L = map(int, input().split())
N = list(range(1,N+1))
l = []
ll = []
for i in N:
  l.append(L+i-1)
  ll.append(abs(L+i-1))
print(sum(l)-l[ll.index(min(ll))])