n1=n2=n3=n4=0
for _ in range(3):
    a,b = map(int,input().split())
    if a==1:
        n1+=1
    elif a==2:
        n2+=1
    elif a==3:
        n3+=1
    else:
        n4+=1
    if b==1:
        n1+=1
    elif b==2:
        n2+=1
    elif b==3:
        n3+=1
    else:
        n4+=1
if n1*n2*n3*n4==4:
    print("YES")
else:
    print("NO")
