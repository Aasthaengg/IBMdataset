S = input()
CF = 'CODEFESTIVAL2016'
ans = 0
for i in range(len(S)):
    if S[i] != CF[i]:
        ans += 1
print(ans)