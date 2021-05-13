h1, m1, h2, m2, K = list(map(int, input().split()))
if (h2 - h1)*60 + (m2-m1) < K:
    print('{}'.format(0))
else:
    print('{}'.format((h2 - h1)*60 + (m2-m1) - K))
