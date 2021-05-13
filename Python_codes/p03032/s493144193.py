# AtCoder
N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for l in range(K+1):
    for r in range(K-l+1):
        if l+r > N:
            break
        d = K-(l+r)

        j = V[:l]+V[N-r:]
        j.sort()

        for i in range(d):
            if not j:
                break
            elif j[0] >= 0:
                break
            j.pop(0)

        ans = max(ans, sum(j))
print(ans)
