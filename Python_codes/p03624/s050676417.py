s = list(str(input()))
s.sort()
a = [chr(ord('a') + i) for i in range(26)]
b = {}
for i in a:
    b[i] = 0
for i in s:
    b[i] += 1

alf = ''
for i in a:
    if b[i] == 0:
        alf = i
        break
if alf:
    print(i)
else:
    print('None')