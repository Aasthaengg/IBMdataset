import sys
n = int(input())
s = list(input())
t = list(input())

if s == t:
    print(n)
    sys.exit()
can = False
for i in range(n):
    if s[i:n] == t[0:(n-i)]:
        can = True
        break
if can:
    print(n + i )
else:
    print(2*n)
