S = input()
tmp = 'CODEFESTIVAL2016'

res = 0
for i in range(len(S)):
    if S[i] != tmp[i]:
        res += 1
        
print(res)