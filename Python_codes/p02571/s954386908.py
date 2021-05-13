S = input()
T = input()
ans = 0
for i in range(len(S)):
    cnt = 0
    if (i+len(T)-1)==len(S):
        break
    for j in range(len(T)):
        if T[j]==S[i+j]:
            cnt += 1
    ans = max(ans,cnt)

print(len(T)-ans)
