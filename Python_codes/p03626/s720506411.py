import sys
input = sys.stdin.readline
n = int(input())
s = [''] * 2
s[0] = input().strip()
s[1] = input().strip()
mod = 10 ** 9 + 7
if n == 1:
    print(3)
    exit()
if s[0][0] == s[1][0]:
    ans = 3
    j = 1
    if s[0][1] == s[1][1]:
        ans *= 2
        j += 1
elif s[0][0] == s[0][1]:
    ans = 6
    j = 2

while j < n:
    if s[0][j] == s[1][j]:
        if s[0][j-1] == s[1][j-1]:
            ans = (ans * 2) % mod
        j += 1
    else:
        if s[0][j-1] == s[1][j-1]:
            ans = (ans * 2) % mod
        else:
            ans = (ans * 3) % mod
        j += 2

print(ans)