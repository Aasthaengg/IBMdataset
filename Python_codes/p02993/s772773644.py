s = input()
pre = ''

for c in s:
    if pre == c:
        print('Bad')
        exit()
    pre = c

print('Good')
