from datetime import datetime
h1, m1, h2, m2, k = list(map(int, input().split()))
t1 = datetime(2000, 1, 1, h1, m1, 0)
t2 = datetime(2000, 1, 1, h2, m2, 0)
t = (t2 - t1).seconds // 60
ans = t - k
print(ans)