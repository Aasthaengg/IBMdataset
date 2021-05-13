N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for A in range(min(N, K)+1):
    for B in range(min(N, K)+1-A):
        hand = V[:A]+V[N-B:]
        hand.sort()
        i = 0
        while i < K-A-B and i < len(hand) and hand[i] < 0:
            hand[i] = 0
            i += 1
        ans = max(ans, sum(hand))
print (ans)