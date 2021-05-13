n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = [A - B for A,B in zip(a,b)]
if sum(l) < 0:
    print(-1)
    exit()

nega = [i for i in l if i < 0]
posi = [i for i in l if i > 0]
nega.sort()
posi.sort()

p = 0
ans = 0
for n in nega:
    ans += 1
    p += n
    if p <= 0 and posi:
        # 補給
        p += posi.pop()
        ans += 1

print(ans)