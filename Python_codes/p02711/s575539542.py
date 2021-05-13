n = str(input())
tmp = 0
for i in range(len(n)):
    if n[i] == '7':
        tmp = 1
        break
if tmp == 1:
    print('Yes')
else:
    print('No')