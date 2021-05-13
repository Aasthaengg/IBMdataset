s = input()
num = len(s)
'''
WBWBWBWBWB
9ko
'''
temp = s[0]
ans = 0
for i in range(1, num):
    if (temp == s[i]):
        pass
    else:
        ans += 1
        temp = s[i]

print(ans)
