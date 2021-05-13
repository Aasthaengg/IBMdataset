s=input()
n=len(s)
c,m=0,0
l='ACTG'
for i in range(n):
    if(s[i] in l):
        c+=1
        m=max(c,m)
    else:
        c=0
m=max(c,m)
print(m)
