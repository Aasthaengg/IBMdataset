n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
min_nk = min(n, k)
for l in range(min_nk+1):
    for r in range(min_nk-l+1):
        hand = []
        for i in range(l):
            hand.append(v[i])
        for i in range(r):
            hand.append(v[n-1-i])
        hand.sort()
        
        for i in range(min(k-l-r, len(hand))):
            if hand[i] < 0:
                hand[i] = 0
        ans = max(ans, sum(hand))
print(ans)