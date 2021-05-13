n=input()
c=1
m=0
for i in range(1,4):
    if(n[i]==n[i-1]):
        c=c+1
        m=max(m,c)
    else:
        c=1
if(m>=3):
    print("Yes")
else:
    print("No")
