N = int(input())
memo = {}
for i in range(N):
    s = input()
    if s in memo:
        memo[s] += 1
    else:
        memo[s] = 1

M = int(input())
for i in range(M):
    t = input()
    if t in memo:
        memo[t] -= 1
    else:
        memo[t] = -1

score = sorted(memo.items(), key=lambda x:-x[1])
print(max(score[0][1],0))