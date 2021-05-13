n,l = map(int, input().split())
a = [i+l-1 for i in range(1, n+1)]
aabs = [abs(i) for i in a]
print(sum(a) - a[aabs.index(min(aabs))])