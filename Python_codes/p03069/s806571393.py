n = int(input())
s = input()
ss = list(s)[::-1]

white = 0
black = 0
w = [0] * n
b = [0] * n

for i in range(n):
    if s[i] == '#':
        black += 1
    if ss[i] == '.':
        white += 1
    b[i] = black
    w[-i-1] = white

ans = 10**9

for i in range(n):
    if b[i] + w[i] < ans:
        ans = b[i] + w[i]

print(ans-1)