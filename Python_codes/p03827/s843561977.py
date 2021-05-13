n=int(input())
s=input()
c=0
l=[0]

for i in range(n):
    if s[i]=='I':
        c+=1
        l.append(c)
    else:
        c-=1
        l.append(c)
        
print(max(l))