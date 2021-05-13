s = input()
cnt_1 = 0

for i in s:
    if i == '1':
        cnt_1 += 1
        
print(min(cnt_1, len(s) - cnt_1) * 2)