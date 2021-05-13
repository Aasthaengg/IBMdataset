n = input()
a = map(int,raw_input().split())
a.sort()
print a[0],a[n-1],sum(a)