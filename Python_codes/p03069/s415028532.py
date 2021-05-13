N = int(input())
S = input()

if len(set(S)) == 1:
    print(0)
    exit()

b = 0
w = 0
stones = [(0,0)]
for i in S:
    if i == "#":
        b += 1
    else:
        w += 1
    stones.append((b,w))

bb = S.count("#")
ww = S.count(".")

ans = 1e9

for b,w in stones:
    ans = min(ans,b+ww-w)

print(ans)
