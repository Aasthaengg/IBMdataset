S = input()
n = len(S) // 2

cnt = 0
for i in range(n):
    if S[i] != S[-(i+1)]:
        cnt += 1
print(cnt)