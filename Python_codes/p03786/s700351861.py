N=int(input())
A=[int(i) for i in input().split()]
A.sort()
imos=[a for a in A]
for i in range(N-1):
    imos[i+1]+=imos[i]
#print(A)
#print(imos)
for i in range(N-2,-1,-1):
    if 2*imos[i]<A[i+1]:
        print(N-1-i)
        break
else:
    print(N)
