n=int(input())
s=input()
d=0
m=0
for i in s:
    if(i=='D'):
        d-=1
    else:
        d+=1
    m=max(m,d)
print(m)
