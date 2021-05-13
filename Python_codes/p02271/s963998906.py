n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

S = set([])
for i in range(2<<n):
    num = 0
    for j in range(n):
        bit = (i>>j) & 1
        num += bit * A[j]
    S.add(num)

for m in M:
    if m in S:
        print('yes')
        continue
    print('no')

