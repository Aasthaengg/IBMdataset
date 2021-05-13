S = input()
N = len(S)

cnt = 0
ans = 0
for i in range(N):
    if cnt >= 1:
        if S[i] == 'g':
            ans += 1
        cnt -= 1
    else:
        if S[i] == 'p':
            ans -= 1
        cnt += 1
    
print(ans)