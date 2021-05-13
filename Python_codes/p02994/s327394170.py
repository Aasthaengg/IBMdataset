N,L=list(map(int,input().split()))
l=list(range(L,N+L))
l_a=[abs(i) for i in l]
print(sum(l)-min(l_a)) if min(l_a) in l else print(sum(l)+min(l_a))