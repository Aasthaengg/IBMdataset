def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, M = MI()
love = [0] * M
ans = 0

for i in range(N):
    K, *A = MI()
    for a in A:
        love[a - 1] += 1
    
for l in love:
    if l == N:
        ans += 1

print(ans)