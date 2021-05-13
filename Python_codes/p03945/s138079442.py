S = input()

pre = S[0]
res = 0
for i in range(1, len(S)):
    if pre != S[i]:
        res += 1
        pre = S[i]

print(res)
