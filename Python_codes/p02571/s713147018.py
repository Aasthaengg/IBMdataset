s = input("")
t = input("")

ans = 10000

for i in range(len(s)-len(t)+1):
    cnt = 0
    S = s[i:i+len(t)]
    for j in range(len(t)):
        if S[j] != t[j]:
            cnt += 1
    ans = min(ans,cnt)
    
print(ans)