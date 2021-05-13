s = input()
c = ["A","C","G","T"]
ans = 0
count = 0
f = False
for i,ss in enumerate(s):
    if i == 0 and s[i] in c:
        count = 1
        f = True
        continue
    if f:
        if s[i] in c:
            count += 1
        else:
            ans = max(count,ans)
            count = 0
            f = False
    else:
        if s[i] in c:
            count += 1
            f = True
ans = max(count,ans)
print(ans)






