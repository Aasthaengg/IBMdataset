n=int(input())
s=input()
a=[]
now=0
for i in s:
    a.append(now)
    if i=="W":
        now+=1
    
now=0
for i in range(n):
    a[n-i-1]+=now
    if s[n-i-1]=="E":
        now+=1
    
a=sorted(a)
print(a[0])