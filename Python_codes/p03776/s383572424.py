from collections import Counter

C = [[0]*(61) for _ in range(61)]

for i in range(61):
    C[i][0] = 1
    
    for j in range(1, 61):
        C[i][j] = C[i-1][j-1]+C[i-1][j]

N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
cnt1 = Counter(v)
S = sum(v[:A])
print(S/A)

ans = 0

for i in range(A, B+1):
    s = sum(v[:i])
    
    if s*A!=S*i:
        break
    
    cnt2 = Counter(v[:i])
    mark = v[:i][-1]
    ans += C[cnt1[mark]][cnt2[mark]]

print(ans)