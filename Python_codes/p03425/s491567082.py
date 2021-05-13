import itertools
n=int(input())
s=[input()for i in range(n)]
m,a,r,c,h=0,0,0,0,0
for i in s:
 if i[0]=="M":m+=1
 if i[0]=="A":a+=1
 if i[0]=="R":r+=1
 if i[0]=="C":c+=1
 if i[0]=="H":h+=1
l=[m,a,r,c,h]
ans=0
for i in itertools.combinations(l,3):ans+=i[0]*i[1]*i[2]
print(ans)