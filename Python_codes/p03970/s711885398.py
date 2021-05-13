S = 'CODEFESTIVAL2016'
T = input()
res = 0
for i in range(16):
    if S[i] != T[i]:
        res += 1
print(res)