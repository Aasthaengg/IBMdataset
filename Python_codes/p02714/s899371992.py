N = int(input())
S = input()

count = 0
for d in range(1, N//2+2):
    for i in range(N-2*d):
        if S[i] != S[i+d] and S[i+2*d] != S[i+d] and S[i+2*d] != S[i]:
            count += 1


cntR = cntG = cntB = 0
for i in range(N):
    if S[i] == 'R':
        cntR += 1
    elif S[i] == 'G':
        cntG += 1
    else:
        cntB += 1

ans = cntR*cntG*cntB - count
print(ans)
