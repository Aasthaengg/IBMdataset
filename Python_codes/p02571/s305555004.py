S = input()
T = input()
ans = 99999999
for i in range(len(S)-len(T)+1):
    word = S[i:i+len(T)]
    cnt = 0
    for j in range(len(word)):

        if word[j]!=T[j]:
            cnt+=1
    ans = min(ans,cnt)
print(ans)