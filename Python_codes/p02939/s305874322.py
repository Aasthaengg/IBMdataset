S = list(input())
s = 0
num = 0
ans = 0
for i in range(len(S)):
    if i < num:
        continue
    for j in range(1,len(S)-i+1):
        if S[i:i+j] != s:
            s = S[i:i+j]
            num = i+j
            ans += 1
            break
print(ans)