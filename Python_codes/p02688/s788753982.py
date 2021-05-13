# Trick or Treat
N, K = map(int,input().split())
sweets = [0]*N
for _ in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for a in A:
        sweets[a-1] += 1
ans = sum([e == 0 for e in sweets])
print(ans)