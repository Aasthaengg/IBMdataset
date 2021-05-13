s = input()
cnt = 0
p = s[0]
for i in s[1:]:
    if p != i:
        cnt += 1
    p = i
print(cnt)