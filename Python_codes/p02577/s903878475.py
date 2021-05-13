l = list(map(int, input()))
s = 0
for i in l:
    s += i
if s % 9 == 0:
    print('Yes')
else:
    print('No')
