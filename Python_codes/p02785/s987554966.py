n, k = map(int, input().split())
h = list(map(int, input().split()))
sh = sorted(h)
new = list()
if n > k:
    for i in range(n-k):
        new.append(sh[i])
    print(sum(new))
else:
    print(0)