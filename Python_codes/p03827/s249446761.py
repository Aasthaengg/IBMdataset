N = int(input())
S = input().strip()
x = 0
xmax = 0
for i in range(N):
    if S[i]=="I":
        x += 1
        xmax = max(xmax,x)
    else:
        x -= 1
print(xmax)