S = input()
n = len(S)
cnt = 0
for i in range(n-1):
    if S[i]!=S[i+1]:
        cnt += 1
print(cnt)