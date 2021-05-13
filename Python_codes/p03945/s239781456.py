S = list(input())
l = len(S)
cnt = 0
for i in range(1,l):
    if S[i-1] != S[i]:
        cnt += 1
print(cnt)
