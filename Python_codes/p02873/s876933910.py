S = list(input())
N = len(S)+1
cnt = [0] * N
j = 0
k = 0

for i in range(N-2):
    if S[i] == S[i+1]:
        k += 1
    
    else:
        k += 1
        cnt[j] = k
        j += 1
        k = 0

if S[N-2] == S[N-3]:
    cnt[j] = k + 1
else:
    cnt[j] = 1

ans = 0
if S[0] == "<":
    st = 0
else:
    ans += cnt[0]*(cnt[0]+1)//2
    st = 1

for k in range(st,N,2):
    if cnt[k] != 0:
        m = min(cnt[k],cnt[k+1])
        M = max(cnt[k],cnt[k+1])
        ans += m*(m-1)//2 + M*(M+1)//2 
    else:
        break
print(ans)