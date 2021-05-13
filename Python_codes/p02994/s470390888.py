N,L=map(int,input().split())
li=[]
for i in range(N):
    li.append(L+i+1-1)
A=True
li.sort()
S=sum(li)
for j in range(N-1):
    if abs(li[j])<=abs(li[j+1]):
        S-=li[j]
        A=False
        break

if A==True:
    S-=li[N-1]

print(S)
