n,k = map(int,input().split())
x = (n-1)*(n-2)//2-k
if x < 0:
    print(-1)
    exit()
print(n*(n-1)//2-k)
for i in range(2,n+1): print(1,i)
cnt = 0
for i in range(2,n+1):
    for j in range(i+1,n+1):
        if cnt == x: exit()
        print(i,j)
        cnt += 1