import itertools 
N, M, Q = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(Q)]
ans= 0
AA = [i for i in range(1, M+1)]
A = []
for i in sorted(list(itertools.combinations_with_replacement(AA, N))):
    A.append(i)

for i in A:
    result = 0
    for j in range(Q):
        if i[li[j][1]-1]-i[li[j][0]-1] == li[j][2]:
            result += li[j][3]
    ans = max(ans, result)

print(ans)