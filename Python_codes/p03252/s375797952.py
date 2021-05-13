s,t=[sorted(t.count(i)for i in set(t))for t in open(0)]
print('YNeos'[s!=t::2])