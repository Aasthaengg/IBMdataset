A,B,C=map(int,input().split())

if A%2==0 or B%2==0 or C%2==0:
    print(0)
else:
    r1=(A//2)*B*C
    b1=(A-A//2)*B*C
    val1=abs(r1-b1)
    r2=A*(B//2)*C
    b2=A*(B-B//2)*C
    val2=abs(r2-b2)
    r3=A*B*(C//2)
    b3=A*B*(C-C//2)
    val3=abs(r3-b3)
    ans=min(val1,val2,val3)
    print(ans)