N = int(input())
a = [int(input()) for _ in range(N)]
s = [0] * N
c = 0
OK = False
n = 0
while True:
    c += 1
    n = a[n] - 1
    if n == 1:
        OK = True
        break
    if s[n] == 1:
        break
    s[n] = 1
if OK:
    print(c)
else:
    print(-1)