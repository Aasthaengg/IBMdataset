N=int(input())
A=list(map(int,input().split()))

K=0
for a in A:
    while a%2==0:
        K+=1
        a//=2
print(K)
