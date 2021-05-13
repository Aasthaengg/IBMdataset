s=input()
k=int(input())
L=len(s)
ss=[]
for i in range(L):
    for j in range(1,k+1):
        ss.append(s[i:i+j])
t=set(ss)
u=list(t)
u.sort()
print(u[k-1])
