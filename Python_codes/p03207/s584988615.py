n=int(input())
P=[]
for i in range(n):
    P.append(int(input()))
pmax = max(P)
psum = sum(P)
ans = psum-(pmax//2)
print(ans)