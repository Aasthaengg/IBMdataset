s = input()
target = 'CODEFESTIVAL2016'
res = 0
for i in range(16):
    if s[i] != target[i]:
        res += 1
print(res)
