s = input()

n = list(s)

check = False
isok = True

if n[0] == 'A':
    check = True

count = 0

for i in range(2, len(n) - 1):
    if n[i] == 'C':
        count += 1

for i in range(len(n)):
    p = int(ord(n[i]))
    if p == 65 or p == 67 or p > 96:
        continue
    else:
        isok = False

if check and count == 1 and isok:
    print('AC')
else:
    print('WA')


