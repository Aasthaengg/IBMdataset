n = int(input())
la = [int(w) for w in input().split()]
lb = [int(w) for w in input().split()]
ld = [a-b for a, b in zip(la, lb)]
if sum(ld) < 0:
    print(-1)
    exit()

llower = [w for w in ld if w < 0]
lupper = [w for w in ld if w > 0]
lowsum = sum(llower)
lupper.sort(reverse=True)

ans = len(llower)

for d in lupper:
    if lowsum >= 0:
        break
    ans += 1
    lowsum += d


print(ans)
