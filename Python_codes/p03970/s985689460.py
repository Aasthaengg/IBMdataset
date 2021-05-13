S = input()
r = 'CODEFESTIVAL2016'
cnt = 0
for i in range(16):
    if S[i] != r[i]:
        cnt += 1
print(cnt)