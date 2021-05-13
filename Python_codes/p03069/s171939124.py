n=int(input())
s=input()
c=[0]
for i in range(n):
    c.append(c[i]+(s[i]=='#'))
p=n
for i in range(n+1):
    p=min((n-c[-1]+c[i])+(c[i]-i),p)
print(p)