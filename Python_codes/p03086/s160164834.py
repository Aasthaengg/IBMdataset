s = input()

ans = 0
flag = True
li = ['A', 'C', 'G', 'T']

tmp = 0
for each in s:
    if each in li:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0

print(ans)