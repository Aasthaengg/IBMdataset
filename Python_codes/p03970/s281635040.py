s1 = input()
s2 = 'CODEFESTIVAL2016'
ans = 0
for i in range(min(len(s1), len(s2))):
    if s1[i] != s2[i]:
        ans += 1
print(ans)
