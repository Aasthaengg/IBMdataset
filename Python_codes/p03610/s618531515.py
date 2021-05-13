S = list(input())
res = []
for i in range(len(S)):
    if (i+1)%2:
        res.append(S[i])
print(''.join(res))