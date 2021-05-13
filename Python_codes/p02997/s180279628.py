n,k = map(int,input().split())

max_k = (n-1)*(n-2)//2
if(max_k < k):
    print(-1)
    exit()

m = (n-1) + (max_k - k)
print(m)

for i in range(2,n+1):
    print(' '.join(map(str,[1,i])))

now = max_k
for i in range(2,n):
    for j in range(i+1,n+1):
        if(now == k):
            exit()
        print(' '.join(map(str,[i,j])))
        now -= 1