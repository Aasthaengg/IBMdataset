import sys

n = list(input())
n1 = ['R','S','R']

i = 0
cou = 0
if n == n1:
    print(1)
    sys.exit()
while i != len(n):
    if n[i] == 'R':
        cou += 1
    i += 1
print(cou)