N=int(input())
S=[]
for i in range(0,N):
    t=str(input())
    S.append(t)
u=set(S)
w=list(u)
print(len(w))