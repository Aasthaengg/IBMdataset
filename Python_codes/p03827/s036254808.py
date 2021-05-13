from sys import stdin
def S(): return stdin.readline().rstrip()
def I(): return int(stdin.readline().rstrip())

n = I()
s = S()

ans = 0
x = 0

for i in range(n):
    if s[i] == 'I':
        x += 1
        if ans < x:
            ans = x
    else:
        x -= 1

print(ans)