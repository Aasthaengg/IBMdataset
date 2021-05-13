a,b,c = map(int,raw_input().split(" "))
print sum([1 for i in range(a,b+1) if c % i == 0])