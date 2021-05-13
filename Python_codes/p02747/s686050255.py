s = input()
ans = ''
flag = False
for i in range(5):
    ans += 'hi'
    if ans == s:
        flag = True
print('Yes' if flag else 'No')
