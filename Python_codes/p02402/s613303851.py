input()
a = list(map(lambda x : int(x), input().split(" ")))
print("%d %d %d" % (min(a), max(a), sum(a)))