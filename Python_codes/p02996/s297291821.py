n = int(input())
abl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((b,a))

abl.sort()
curr = 0
for b,a in abl:
    curr += a
    if curr > b:
        print('No')
        break
else:
    print('Yes')