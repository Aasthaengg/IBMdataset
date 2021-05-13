n,m = map(int, raw_input().split(' '))
print sum([1 for e in  map(int, raw_input().split(' ')) if e >= m] or [0])
