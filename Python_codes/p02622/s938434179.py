s=input()
t=input()
c=0
for s1,t1 in zip(s,t):
    c+=s1!=t1
print(c)