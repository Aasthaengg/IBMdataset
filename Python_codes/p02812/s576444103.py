N,S = open(0).read().split()
N = int(N)
ans = 0
for i in range(N-2):
    if S[i:i+3] == 'ABC':
        ans += 1
print(ans)