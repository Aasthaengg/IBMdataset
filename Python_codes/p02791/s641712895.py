N = int(input())
P = list(map(int,input().split()))

n = N+1
cnt = 0
for i in P:
    if i <= n:
        cnt += 1
        n = i

print(cnt)