import sys

N = int(input())

print(0)
ans_f = input()

if ans_f == "Vacant":
    sys.exit()

l = 0
r = N-1
ans = ''
while r - l > 1:
    c = (l+r)//2
    print(c)
    ans = input()
    if ans == 'Vacant':
        sys.exit()
    if (ans == ans_f and c % 2 == 0) or (ans != ans_f and c % 2 == 1):
        l = c
    else:
        r = c

print(r)
ans = input()
if ans == 'Vacant':
    sys.exit()




