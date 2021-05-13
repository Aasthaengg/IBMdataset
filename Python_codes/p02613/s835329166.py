n = int(input())
l = ["AC", "WA", "TLE", "RE"]
d = {k: 0 for k in l}
for _ in range(n):
    s = input()
    d[s] += 1
for k in l:
    print("{} x {}".format(k, d[k]))