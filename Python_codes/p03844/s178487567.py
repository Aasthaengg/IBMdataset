A,OP,B=input().split()

a,b=int(A),int(B)
op=str(OP)

if op =='+':
    ans=a+b
else:
    ans=a-b
    
print(ans)