t=sorted(map(int,open(0).read().split()))
print(['YES','NO'][max([t.count(i)for i in range(1,5)])>2])