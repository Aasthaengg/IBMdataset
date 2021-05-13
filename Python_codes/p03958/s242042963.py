K,T,*a = map(int, open(0).read().split())
a.sort()
print(max(0,a[-1]-sum(a[:T-1])-1))