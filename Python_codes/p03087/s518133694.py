N, Q = map(int, input().split())
S = input()
memo = [0]

tmp = 0
for i in range(1, N):
    if S[i-1]+S[i] == "AC":
        tmp += 1
    memo.append(tmp)

for _ in range(Q):
    l, r = map(int, input().split())
    print(memo[r-1] - memo[l-1])
