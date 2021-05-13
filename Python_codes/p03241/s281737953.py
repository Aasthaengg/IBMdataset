N ,M = map(int,input().split())
L = []
for i in range(1,int(M**(1/2)+1)):
    if M % i == 0:
        L.append((i,M//i))
ans = 0
for x in L:
    if x[1] >= N:
        ans = max(ans,x[0])
    if x[0] >= N:
        ans = max(ans,x[1])
print(ans)
