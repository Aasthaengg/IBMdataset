N,D = map(int,input().split())
ans = 0

for i in range(N):
    x, y = map(int,input().split())
    if pow(x,2)+pow(y,2)<=pow(D,2):
        ans+=1
print(ans)
