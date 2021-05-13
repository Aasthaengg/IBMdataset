N=int(input())
L=list(map(int,input().split()))
L=[j-i for i,j in enumerate(L,1)]
L.sort()
A=(L[N//2]+L[(N-1)//2])//2
print(sum([abs(i-A) for i in L]))