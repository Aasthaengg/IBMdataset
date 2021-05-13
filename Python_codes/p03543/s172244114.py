n = input()
pre, count = n[0], 1
for i in n[1:]:
    if pre == i:
        count += 1
        if count == 3:
            break
    else:
        pre = i
        count = 1
if count == 3: print('Yes')
else: print('No')
