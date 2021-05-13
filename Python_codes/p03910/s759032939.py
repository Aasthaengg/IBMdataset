N=int(input())
n=0
S=1
while S<N:
    n+=1
    S=n*(n+1)//2

if N==1:
    print(1)

for i in range(1,n+1):
    if i!=S-N:
        print(i)