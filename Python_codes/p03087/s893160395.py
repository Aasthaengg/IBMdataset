N, Q = map(int, input().split())
S = input()

cnt = [0]*N
i = 0
while i < N-1:
    if S[i:i+2] == "AC":
        cnt[i] += 1
        i += 1
    i += 1

AS = [0]*(N+1)
for i in range(1, N+1):
    AS[i] = AS[i-1] + cnt[i-1]

for i in range(Q):
    l, r = map(int, input().split())
    ans = AS[r-1] - AS[l-1]
    print(ans)