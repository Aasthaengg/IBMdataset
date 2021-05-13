n=int(input())
ab = []
for _ in range(3):
    s=list(input())
    ab.append(s)

ans = 0

for i in range(n):
    memo = []
    for j in range(3):
        memo.append(ab[j][i])
    ans += len(set(memo))-1
    
print(ans)