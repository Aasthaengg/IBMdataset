a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
l=[a,b,c,d,e]
s=[]
t=[]
x=0
for i in range(5):
    s.append(l[i]%10)
for i in range(5):
    if s[i]==0:
        t.append(l[i])
    else:
        t.append((l[i]//10+1)*10)
        
for i in range(1,10):
    if s.count(i)>0:
        x=10-i
        break
print(sum(t)-x)