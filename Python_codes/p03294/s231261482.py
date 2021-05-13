N=int(input())
a=list(map(int,input().split()))


S=0
for k in range(N):
        S+=a[k]-1
print(S)