import sys
n = int(input())
x = [list(map(int, x.split())) for x in sys.stdin.readlines() ]
x.reverse()
ans = 0
for i in x:
    a, b = map(int, i)
    if (a+ans)%b != 0:
        ans += b - (a+ans)%b
print(ans)