c11, c12,c13=[int(i) for i in input().split()]
c21, c22,c23=[int(i) for i in input().split()]
c31, c32,c33=[int(i) for i in input().split()]

ans=0
for a1 in range(c11+1):
    b1=c11-a1
    b2=c12-a1
    b3=c13-a1
    a2=c21-b1
    a3=c31-b1
    
    if c22==a2+b2 and c23==a2+b3 and c32==a3+b2 and c33==a3+b3:
        print("Yes")
        ans=1
        break

if ans==0:
    print("No")