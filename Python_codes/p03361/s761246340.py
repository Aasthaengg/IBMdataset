h,w=map(int,input().split())
s=[[] for i in range(h+2)]
for i in range(h):
    x=input()
    x="."+x
    x=x+"."
    s[i+1]=list(x)
s[0]=["." for i in range(w+2)]
s[-1]=["." for i in range(w+2)]
f=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j]=="#" and s[i][j+1]==s[i][j-1]==s[i+1][j]==s[i-1][j]==".":
            f=1
print("Yes" if f==0 else "No")
