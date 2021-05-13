N = int(input())
S = input()
WL = 0
WR = 0
BL = 0
BR = 0

for i in range(N):
    if S[i] == '#':
        BR += 1
    else:
        WR += 1

ans = BL+WR

for i in range(N):
    if S[i] == '#':
        BR -= 1
        BL += 1
    else:
        WR -= 1
        WL += 1
    ans = min(ans,BL+WR)
print(ans)
