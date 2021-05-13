n=int(input())
s=input()
lCurrent=rCurrent=0
l=[0]*n
r=[0]*n
ans=[0]*n

for i in range(n-1):
    if s[i]=="W":
        lCurrent+=1
    l[i+1]=lCurrent

for i in reversed(range(1,n)):
    if s[i]=="E":
        rCurrent+=1
    r[i-1]=rCurrent

ans=[x+y for x,y in zip(l,r)]
print(min(ans))