n = int(input())
s = input()

d = {}
for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

ans = 1
for x in d.values():
    ans *= x+1

print((ans - 1) % (10**9+7))