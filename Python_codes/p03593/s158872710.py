from collections import Counter
H, W = map(int,input().split())
a = ""
for k in range(H):
    a += input()
C = Counter(a)
s = 0
for e in C:
    s += C[e]//4
if s < (H//2)*(W//2):
    print("No")
    exit(0)

a = s-(H//2)*(W//2)
t = 0
u = 0
for e in C:
    t += C[e]%4
    u += C[e]%2

if 2*t + 4*a < (H%2)*(H//2) + (W%2)*(W//2):
    print("No")
    exit(0)
if u != (H%2)*(W%2):
    print("No")
else:
    print("Yes")
