n, m = map(int, open(0).read().split())
if n < 10:
    print(m+100*(10-n))
else:
    print(m)