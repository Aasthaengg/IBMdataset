# 解説動画視聴

s = input()

a = [0]*(len(s)+1)
if len(s) == 1:
    print(1)
    exit()
for i in range(len(s)):
    if s[i] == '<':
        a[i+1] = max(a[i+1],a[i]+1)
for i in range(len(s)-1,-1,-1):
    if s[i] == '>':
        a[i] = max(a[i],a[i+1]+1)

print(sum(a))