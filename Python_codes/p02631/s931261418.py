N = int(input())
A = list(map(int, input().split()))
maxl = len(bin(max(A))[2:])
ans = [['0'] * N for _ in range(maxl)]
for n in range(N):
    for d, a in enumerate(bin(A[n])[2:].zfill(maxl)):
        ans[d][n] = a

for dn in range(maxl):
    n1 = sum([1 for d in ans[dn] if d == '1'])
    if n1 % 2 == 1:
        for n in range(N):
            ans[dn][n] = '0' if ans[dn][n] == '1' else '1'

prt = [int(''.join([ans[d][n] for d in range(maxl)]), 2) for n in range(N)]
print(' '.join(map(str, prt)))
