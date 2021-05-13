from sys import stdin

s = list(stdin.readline().rstrip())

ans = True

odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']

for i, t in enumerate(s):
    if (i+1)%2 == 1:
        if not t in odd:
            ans = False
    else:
        if not t in even:
            ans = False

if ans:
    print('Yes')
else:
    print('No')