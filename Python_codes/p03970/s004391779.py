s = input()
tar = 'CODEFESTIVAL2016'
res = 0
for i in range(len(s)):
    if s[i] != tar[i]:
        res +=1
print(res)