# coding: utf-8
s = input()
origin = list('CODEFESTIVAL2016')
ans = 0

for index, ch in enumerate(list(s)):
    if origin[index] != ch:
        ans += 1

print(ans)