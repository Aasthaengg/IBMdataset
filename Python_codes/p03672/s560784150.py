s = input()

n = -1
if len(s) % 2 == 0:
    n = -2
while len(s) > abs(n):
    hanbun = len(s[:n])//2
    if s[:hanbun] == s[hanbun:n]:
        print(len(s[:n]))
        break
    n -= 2