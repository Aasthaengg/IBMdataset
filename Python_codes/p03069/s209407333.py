N,S = open(0).read().split()
N = int(N)
w = S.count('.')
ans = float('inf')
ws = [0] * (N+1)
for i in range(1,N+1):
    ws[i] = ws[i-1]
    if S[i-1] == '.':
        ws[i] += 1
for i in range(N+1):
    ans = min(ans,i-2*ws[i]+w)
print(ans)