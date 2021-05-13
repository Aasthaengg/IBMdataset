s = input()
size = len(s)
b_num = 0
w_num = 0

for each in s:
    if each == 'W':
        w_num += 1
    else:
        b_num += 1

ans = 0
b_left = w_num
for i in range(size):
    if s[i] == 'B':
       ans += b_left - i
       b_left += 1

print(ans)