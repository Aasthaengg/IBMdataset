N,M=map(int,input().split())
cnt = [0]*N
for _ in range(M):
    a,b=map(int,input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1
print("YES" if all([cnt[i] % 2 == 0 for i in range(N)]) else "NO")