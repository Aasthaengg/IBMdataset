N, K, C = map(int, input().split(" "))
S = input()

L = [0]     # L[i]->前から決めてi回目に働く日
R = []      # R[i]->後ろから決めてi回目に働いていなければいけない日

i = 0
while i < N:
    if S[i] == 'o':
        L.append(i + 1)
        i += C
    i += 1

i = N - 1
while i > -1:
    if S[i] == 'o':
        R.append(i + 1)
        i -= C
    i -= 1
R.append(0)
R.reverse()

ans = []
for i in range(1, K + 1):
    if L[i] == R[i]:
        ans.append(L[i])


if min(len(L), len(R)) > K + 1:
    print()
else:
    print('\n'.join([str(a) for a in ans]))
