import sys

N, K = map(int, input().split())
S = input()

isOneFound = False
ruiseki = []
if S[0] == "0":
    ruiseki.append(0)

for i in range(N):
    if i == N-1:
        ruiseki.append(i+1)
        continue
    if S[i] != S[i+1]:
        ruiseki.append(i+1)

if S[-1] == "0":
    ruiseki.append(N)

#print(ruiseki)

# 全部ひっくり返せる場合
if K >= (len(ruiseki)-1) // 2:
    print(N)
    sys.exit(0)


l = 0
r = 2 * K
ans = -1
while r < len(ruiseki):
    if l > 0:
        tmp = ruiseki[r] - ruiseki[l-1]
    else:
        tmp = ruiseki[r]
    ans = max(ans, tmp)
    l += 2
    r += 2

print(ans)
