n, *s = map(int, open(0).read().split())
print(sum(s[i+1]-s[i]+1 for i in range(0, n*2, 2)))