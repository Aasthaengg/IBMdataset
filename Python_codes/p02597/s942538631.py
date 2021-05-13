n = int(input())
S = input()

r = S.count('R')
w = len(S)-r

if r == 0 or w == 0:
    print(0)
    exit()

ans = 0
for i in range(len(S)):
    if S[i] == "R":
        r -= 1
    else:
        r -= 1
        w -= 1
        ans += 1
    if r == 0 or w == 0:
        break
print(ans+r)