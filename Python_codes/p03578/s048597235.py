N = int(input())
D = list(map(int,input().split()))

M = int(input())
T = list(map(int,input().split()))

memo = {}

for d in D:
    if d in memo:
        memo[d] += 1
    else:
        memo[d] = 1
        
for t in T:
    if t in memo and 0 < memo[t]:
        memo[t] -= 1
    else:
        print('NO')
        exit()
print('YES')
