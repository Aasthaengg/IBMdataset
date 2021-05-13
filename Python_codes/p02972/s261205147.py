N = int(input())
a = [-1]+list(map(int,input().split()))
b = [0]*(N+1)
for i in range(N,0,-1):
    su = 0
    j = 2
    while i*j <= N:
        su += b[i*j]
        j+=1
    b[i] = (a[i]+su)%2

if sum(b)>0:
    print(sum(b))
else:
    print(0)
    exit()

ans =[]
for i in range(1,N+1,1):
    if b[i]==1:
        ans.append(i)
print(*ans)