# B
S = input()
w = int(input())
ans = S[0]
cnt = 1
for i in range(1, len(S)):
    if cnt == w:
        ans += S[i]
        cnt = 0
    cnt += 1
print(ans)