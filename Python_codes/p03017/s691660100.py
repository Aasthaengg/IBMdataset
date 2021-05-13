def no():
    print("No")
    exit()

n, a, b, c, d = map(int, input().split())
s = list(input())
for i in range(a - 1, c - 1):
    if s[i] == s[i + 1] == "#":
        no()
for i in range(b - 1, d - 1):
    if s[i] == s[i + 1] == "#":
        no()
if c > d:
    t = 0
    for i in range(b - 2, d - 1):
        if s[i] == s[i + 1] == s[i + 2] == ".":
            t = 1
    if t == 0:
        no()
print("Yes")