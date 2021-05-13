N = int(input())
S = list(input())

d = S.count('D')
i = S.count('I')
cnt = 0
cntold = 0
for n in range(N):
    if S[n] == 'D':
        cnt -= 1
    else:
        cnt += 1
    
    if cnt > cntold:
        cntold = cnt
print(cntold)