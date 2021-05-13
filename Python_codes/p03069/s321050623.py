n = int(input())
s = input()

wlist = [0] * (n + 1)
blist = [0] * (n + 1)

for i in range(n):
    if s[i] == ".":
        wlist[i + 1] = wlist[i] + 1
        blist[i + 1] = blist[i]
    elif s[i] == "#":
        wlist[i + 1] = wlist[i]
        blist[i + 1] = blist[i] + 1

ans = n

for i in range(n + 1):
    tmp = blist[i] + (wlist[n] - wlist[i])
    if ans > tmp: ans = tmp
print(ans)