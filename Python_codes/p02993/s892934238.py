# A - Security

# 標準入力S
S = input()
x = 99
j = 0

for i in S:
    if x == i:
        j += 1
    else:
        x = i

if j == 0:
    print('Good')
else:
    print('Bad')
