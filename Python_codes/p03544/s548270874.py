N=int(input())

A=[2,1]
ans=0
if N==1:
    ans=1
else: 
    for _ in range(N-1):
        a=A.pop(0)
        b=A.pop(0)
        c=a+b
        A.append(b)
        A.append(c)
    ans=A[1]

print(ans)
