n = int(input())
ans = 0
sts = dict()
mi = 0
bl = 0

for i in range(n):
    ai = int(input())
    if i-ai >= mi:
        sts[i-ai] = ai
        if bl >= ai:
            mi = i-ai
    else:
        print(-1)
        exit()
    bl = ai

for i in sts.values():
    ans += i
print(ans)
