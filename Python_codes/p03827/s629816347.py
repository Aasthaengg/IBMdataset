N = int(input())
S = input()
x = 0
xmax = 0
for i in range(N):
    if S[i] == "I":
        x += 1
    elif S[i] == "D":
        x -= 1
    if xmax <= x:
        xmax = x
print(xmax)