N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
S=0
for i in L:
    S+=i
S-=L[N-1]
if S>L[N-1]:
    print("Yes")
else:
    print("No")