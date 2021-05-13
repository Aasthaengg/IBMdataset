N,L=map(int,input().split())
T=[]
for i in range(N):
    T.append(L+i)
if L>=1:
    print(sum(T)-T[0])
elif T[N-1]<=-1:
    print(sum(T)-T[N-1])
else:
    print(sum(T))