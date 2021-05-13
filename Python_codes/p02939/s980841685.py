s = list(input())
tmp1 = s[0]
tmp2 = ''
count = 0
for i in range(1, len(s)):
    tmp2 += s[i]
    if tmp2 != tmp1:
        count += 1
        tmp1 = tmp2
        tmp2 = ''
print(count + 1)
