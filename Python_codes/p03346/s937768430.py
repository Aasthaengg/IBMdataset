N=int(input())
P=[int(input()) for i in range(N)]

arr=[(P[i],i) for i in range(N)]
arr.sort()

i=0
L=0

while(i<N):
    j=i
    while(j<N-1 and arr[j+1][1]>arr[j][1]):
        j+=1
    L=max(L,j-i+1)
    i=j+1
print(N-L)