n,a,b,c,d=map(int,input().split())
s=input()
if c<d:
    for i in range(a,d-2):
        if s[i]=="#" and s[i+1]=="#":
            print("No")
            exit()
    print("Yes")
else:
    for i in range(a,c-2):
        if s[i]=="#" and s[i+1]=="#":
            print("No")
            exit()
    i=b-2
    temp=0
    while i<=d:
        if s[i]==".": temp+=1
        else: temp=0
        if temp==3:
            print("Yes")
            exit()
        i+=1
    print("No")