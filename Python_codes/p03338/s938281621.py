n=int(input())
s=input()
a=list("abcdefghijklmnopqrstuvwxyz")
x=[]
y=[]
m=0
for i in range(n-1):
    x=[s[j] for j in range(i)]
    y=[s[j] for j in range(i,n)]
    ans=0
    for j in range(26):
        if a[j] in x and a[j] in y:
            ans+=1
    m=max(ans,m)
print(m)
