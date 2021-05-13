s = input()
a = 'CODEFESTIVAL2016'
cnt = 0
for i in range(16):
    if s[i] != a[i]:
        cnt += 1
print(cnt)