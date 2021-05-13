s = input()
cnt = 0
for i in range(int((len(s)+1)/2)):
    if s[i] != s[-i-1]:
        cnt += 1
print(int(cnt))