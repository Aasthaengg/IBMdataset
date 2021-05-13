n = int(input())
s = input()
cnt_r = 0
cnt_b = 0
for i in range(len(s)):
    if s[i] == 'R':
        cnt_r+=1
    elif s[i] == 'B':
        cnt_b +=1
if cnt_r > cnt_b:
    print('Yes')
else:
    print('No')