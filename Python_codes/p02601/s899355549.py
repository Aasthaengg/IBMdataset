A=list(map(int,input().split()))
K=int(input())
a=A[0]
b=A[1]
c=A[2]
count=0
while count<=K:
    if a>=b:
        b=b*2
        count=count+1
    else:
        break
if count==K:
    pass
else:
    c=c*(2**(K-count))
if a<b<c:
    print("Yes")
else:
    print("No")