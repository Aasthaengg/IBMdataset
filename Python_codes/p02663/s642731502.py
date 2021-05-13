h1, m1, h2, m2, K = list(map(int, input().split()))

diff = (h2-h1) * 60 + m2-m1
print(diff - K)