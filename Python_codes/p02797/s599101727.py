N, K, S = map(int, input().split())

l = []
for i in range(K):
    l.append(str(S))

for i in range(N-K):
    if S == 1:
        l.append(str(S+1))
    else:
        l.append(str(S-1))

print(' '.join(l))