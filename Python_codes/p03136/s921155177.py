N=int(input())
L=list(map(int,input().split()))
Lmax=max(L)
L.remove(max(L))
if Lmax<sum(L):
    print('Yes')
else:
    print('No')