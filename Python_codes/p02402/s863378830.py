n = input()
l = sorted(map(int,raw_input().split()))
print l[0], l[n-1], reduce(lambda x,y: x+y, l)