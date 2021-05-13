s = input()
acgt = ['A','C','G','T']
ans = 0
p = 0
for i in range(len(s)):
    if s[i] in acgt:
        p += 1
    else:
        ans = max(ans,p)
        p = 0
print(max(ans,p))