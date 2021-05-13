H, W = map(int, input().split())
X = [0] * 26
for _ in range(H):
    for a in input():
        X[ord(a)-97] += 1

Y = [0] * 2 # 1, 2
for x in X:
    if x%4 == 1:
        Y[0] += 1
    elif x%4 == 2:
        Y[1] += 1
    elif x%4 == 3:
        Y[0] += 1
        Y[1] += 1

if Y[0] <= (H%2) * (W%2) and Y[1] <= (H%2) * (W//2) + (W%2) * (H//2):
    print("Yes")
else:
    print("No")