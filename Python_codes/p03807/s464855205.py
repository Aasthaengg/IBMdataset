N=int(input())
A=list(map(int,input().split()))

a=0
b=0
for i in range(N):
    val=A[i]
    if val%2==0:
        a+=1
    else:
        b+=1

if b%2==0:
    print("YES")
else:
    print("NO")