N, K = list(map(int,input().rstrip().split()))
H = list(map(int,input().rstrip().split()))
ans = 0
for h in H:
    if h >= K:ans+=1
print(ans)