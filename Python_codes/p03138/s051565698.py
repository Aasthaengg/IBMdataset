N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

X = 0
bit_l = 0
while K >= (1 << bit_l):
    bit_l += 1
bit_l -= 1

while bit_l >= 0:
    one = 0
    for a in A:
        one += int(((a >> bit_l) & 1) == 1)
    if one < N - one and (X | (1 << bit_l)) <= K:
        X = X | (1 << bit_l)
    bit_l -= 1

ans = sum([a ^ X for a in A])
print(ans)