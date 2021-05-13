x = map(int,raw_input().split())
a,b = sorted(x[:2])
print sum([1 for i in range(a,b+1) if x[2]%i==0])