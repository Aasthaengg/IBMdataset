H, W, A, B = map(int,input().split())
S = [1] * A + [0] * (W - A)
T = [0] * A + [1] * (W - A)
s = ""
t = ""
for a in S:
    s += str(a)
for b in T:
    t += str(b)
for _ in range(B):
    print(s)
for _ in range(H - B):
    print(t)