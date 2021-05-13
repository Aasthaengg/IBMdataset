N=int(input())
P=[]
for i in range(N):
    P.append(int(input()))
P.sort()
x=P[N-1]//2
print(sum(P)-x)