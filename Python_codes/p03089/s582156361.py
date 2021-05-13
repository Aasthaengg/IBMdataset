N = int(input())
b = list(map(int,input().split()))

ans = []
for i in range(N):
    for j in range(len(b)-1,-1,-1):
        if b[j]==(j+1):
            ans += [b[j]]
            del b[j]
            break
if len(b)!=0:
    print(-1)
    exit()

for i in range(N):
    print(ans[N-1-i])