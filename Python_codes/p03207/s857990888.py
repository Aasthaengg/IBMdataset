N=int(input())
P=[]
for i in range(N):
    P.append(int(input()))

A=max(P)
print(sum(P)-A//2)