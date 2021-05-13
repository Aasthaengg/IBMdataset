import sys
input = sys.stdin.readline

n = int(input())
sn = [input().strip('\n') for _ in range(n)]

mod = 10**6 + 7
hs = [[0, ''] for _ in range(mod)]

def hypo(s, Mod):
    h_num = 1
    for i in s:
        h_num = h_num * ord(i) % Mod
    return h_num

for s in sn:
    s = ''.join(sorted(s))
    h = hypo(s, mod)
    while True:
        if h >= mod :
            h = 0
        if hs[h][0] == 0:
            hs[h][0] += 1
            hs[h][1] += s
            break
        if hs[h][1] == s:
            hs[h][0] += 1
            break
        h += 1

ans = 0
for j, t in hs:
    if j >= 2:
        ans += j * (j-1) / 2

print(int(ans))
