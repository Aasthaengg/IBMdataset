n=int(input())
x=0
m=0
s=list(input())
for i in range(n):
    if s[i]=="I":
        x+=1
    else:
        x-=1
    m=max(x,m)
print(m)
