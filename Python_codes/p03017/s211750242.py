n,a,b,c,d=map(int,input().split())
a,b,c,d=a-1,b-1,c-1,d-1
s=list(input())
flg=True
for i in range(a,c):
    if s[i]=="#" and s[i+1]=="#":
        print("No")
        exit()
for i in range(b,d):
    if s[i]=="#" and s[i+1]=="#":
        print("No")
        exit()
if c>d:
    flg=False
    for i in range(b,d+1):
        if s[i-1]==s[i]==s[i+1]==".":
            flg=True
if flg:       
    print("Yes")
else:
    print("No")