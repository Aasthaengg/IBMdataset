N, K, C = map(int, input().split())
S = input()
S_reverse = S[::-1]

l = []
r = []

i = 0
while i<N and len(l)<K:
    if S[i] == 'o':
        l.append(i+1)
        i += C+1
    else:
        i += 1

i = 0
while i<N and len(r)<K:
    if S_reverse[i] == 'o':
        r.append(i)
        i += C+1
    else:
        i += 1

r = [N - i for i in r]
r.reverse()

ans = []

# print(l)
# print(r)

for i in range(K):
    if l[i] == r[i]:
        ans.append(l[i])


# exit()
# ans = set(l) & set(r)

# ans = list(ans)
ans.sort()

for i in ans:
    print(i)