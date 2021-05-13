n=int(input())
A=input()
B=input()
C=input()
ans=0
for i in range(n):
    a=A[i]
    b=B[i]
    c=C[i]
    if a==b and b==c:
        pass
    elif a==b or a==c or b==c:
        ans+=1
    else:
        ans+=2
print(ans)