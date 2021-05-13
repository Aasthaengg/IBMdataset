n, a, b, c, d = map(int, input().split())
s = input()
a -= 1; b -= 1; c -= 1; d -= 1; e = 1
for i in range(b, min(c, d)+1):
    if s[i-1] == "." and s[i] == "." and s[i+1] == ".": e = 0
if c < d: e = 0
for i in range(a, max(c, d)):
    if s[i] == "#" and s[i+1] == "#": e = 1
print("Yes") if e == 0 else print("No")