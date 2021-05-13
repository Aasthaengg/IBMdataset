S = input()
N = len(S) + 1

ans = 0

cnt0 = 0
if S[0] == ">":
    cnt0 += 1
    j = 1
    while j <= len(S)-1 and S[j] == ">":
        cnt0 += 1
        j += 1
ans += cnt0*(cnt0+1)//2


for i in range(1, N-1):
    if S[i-1] == "<" and S[i] == ">":
        j = i-1
        k = i+1
        cnt1 = 0
        cnt2 = 0
        if S[i-1] == "<" and i >= 0:
            while j >= 0 and S[j] == S[i-1] :
                cnt1 += 1 
                j -= 1
        if S[i] == ">":
            while k <= N-1 and S[i] == S[k-1]:
                cnt2 += 1
                k += 1 
        ans += max(cnt1, cnt2)*(max(cnt1, cnt2)+1)//2
        ans += (min(cnt1, cnt2)-1)*(min(cnt1, cnt2))//2


cntn = 0
if S[-1] == "<":
    cntn += 1
    j = -2
    while j >= -len(S) and S[j] == "<":
        cntn += 1
        j -= 1
ans += cntn*(cntn+1)//2


print(ans)