s=input()
l=len(s)
t="abcdefghijklmnopqrstuvwxyz"
d={}
for i in t:d[i]=0
for i in s:d[i]+=1
a=l*(l-1)//2
for i in t:a-=d[i]*(d[i]-1)//2
print(a+1)