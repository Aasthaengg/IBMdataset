N, K = map(int, input().split())
S = input()

if(S[0] == "1"):
    s = []
else:
    s = [0]
cnt = 1
tmp = S[0]
for i in range(1, len(S)):
    if(tmp == S[i]):
        cnt += 1
    else:
        s.append(cnt)
        tmp = S[i]
        cnt = 1
s.append(cnt)
tmp1 = 0
if(len(s)//2 <= K):
    ans = sum(s)        
else:
    ans = sum(s[:(2*K+1)])
    tmp = ans
    cnt = 0
    for i in range(2*K+1, len(s)-1, 2):
        if(ans < tmp-s[cnt]-s[cnt+1]+s[i]+s[i+1]):
            ans = tmp-s[cnt]-s[cnt+1]+s[i]+s[i+1]
            tmp = tmp-s[cnt]-s[cnt+1]+s[i]+s[i+1]
        else:
            tmp = tmp-s[cnt]-s[cnt+1]+s[i]+s[i+1]
        cnt += 2
    ss = s[::-1]
    if(S[-1] == "0"):
        tmp1 = sum(ss[:(2*K)])
    else:
        tmp1 = sum(ss[:(2*K+1)])
print(max(ans, tmp1))