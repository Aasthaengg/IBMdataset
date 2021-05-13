n,a,b = map(int, input().split())
print('{0} {1}'.format(min(a,b), 0 if a+b<=n else a+b-n))