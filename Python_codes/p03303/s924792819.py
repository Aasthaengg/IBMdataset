n=input()
s=int(input())
t=len(n)//s
c=""
for i in range((t+1 if len(n)%s!=0else t)):
    c+=n[i*s]
print(c)