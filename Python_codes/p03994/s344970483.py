s = input()
K = int(input())
N = len(s)

S = [0 for _ in range(N)]

for i in range(N):
    S[i] = ord(s[i])-97

tmp = K
ans = ''

for i in range(N):
    if S[i]==0:
        ans += 'a'
    elif 26-S[i] <= tmp:
        ans += 'a'
        tmp -= 26-S[i]
    else:
        ans += s[i]
        
if tmp:
    ans = ans[:-1]+chr((ord(ans[-1])-97+tmp)%26+97)
    
print(ans)