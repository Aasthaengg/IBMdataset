s=input()
cor='CODEFESTIVAL2016'
cnt = 0

for i in range(len(s)):
    if(s[i] != cor[i]):
        c_s = cor[:i+1]+s[i+1:]
        cnt += 1
print(cnt)