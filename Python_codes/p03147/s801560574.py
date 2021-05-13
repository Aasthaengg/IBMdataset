n = int(input())
H = tuple(map(int, input().split()))

def rec(H):
    # Hに0が存在しないと仮定して
    if not H:
        return 0
    ans = min(H)
    H = [h-ans for h in H]

    ranges = []
    preh = 0
    left = -1
    for i, h in enumerate(H):
        # lrを記録
        if preh == 0 and h > 0:
            left = i
        elif preh > 0 and h == 0:
            ranges.append((left, i))
            left = -1
        preh = h
    else:
        if left >= 0:
            ranges.append((left, len(H)))
        
    for l, r in ranges:
        ans += rec(H[l:r])
    return ans

print(rec(H))
