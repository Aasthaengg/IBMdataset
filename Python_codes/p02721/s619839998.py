N, K, C = map(int, input().split())
S = input()

l = []
r = []

i = 0
j = N-1

while i < N and len(l) < K:
    if S[i] == 'o':
        l.append(i)
        i += C
    i += 1

while j >= 0 and len(r) < K:
    if S[j] == 'o':
        r.append(j)
        j -= C
    j -= 1

r.reverse()

for i in range(K):
    if l[i] == r[i]:
        print(l[i]+1)

