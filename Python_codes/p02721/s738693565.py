N, K, C = map(int, input().split())
S = list(input())

R = []
tmp = 0
count = 0
while tmp < N:
    if S[tmp] == 'o':
        R.append(tmp)
        count += 1
        if count == K:
            break
        tmp += C + 1
    else:
        tmp += 1

L = []
tmp = N - 1
count = 0
while tmp >= 0:
    if S[tmp] == 'o':
        L.append(tmp)
        count += 1
        if count == K:
            break
        tmp -= C + 1
    else:
        tmp -= 1

for l, r in zip(R, L[::-1]):
    # print (l, r)
    if l == r:
        print (l + 1)