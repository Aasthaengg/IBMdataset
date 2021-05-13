s = input()
a = 'CODEFESTIVAL2016'
ans = 0
for i in range(0,16):
    if s[i]!=a[i]:
        ans += 1
print(ans)