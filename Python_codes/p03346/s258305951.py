N = int(input())
ps = []
for i in range(N):
    ps.append(int(input()))
memo = {}
for i,p in enumerate(ps):
    memo[p] = 0
    if p-1 in memo:
        memo[p-1] = 1

dct = sorted(memo.items())
result = 0
c = 0
for k,v in dct:
    if v == 1:
        c += 1
    else:
        if c > result:
            result = c
        c = 0
print(N-result-1)