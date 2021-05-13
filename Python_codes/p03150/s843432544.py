s = list(input())
l = len(s)
key = ['k', 'e', 'y', 'e', 'n', 'c', 'e']

# 'keyence' or 'keyence___'
ans_1 = True
for i in range(7):
    if s[i] == key[i]:
        pass
    else:
        ans_1 = False
if ans_1:
    print('YES')
    exit()
else:
    if l == 7:
        print('N0_1')
        exit()

# '___keyence'
ans_2 = True
for i in range(7):
    if s[l-7+i] == key[i]:
        pass
    else:
        ans_2 = False
if ans_2:
    print('YES')
    exit()

# 'k...___...e'
idx = 0
for i in range(7):
    if s[i] == key[i]:
        pass
    else:
        idx = i-1
        break
for i in range(6-idx):
    if s[l-6+idx+i] == key[idx+1+i]:
        pass
    else:
        print('NO')
        exit()
print('YES')