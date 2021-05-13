n,l = map(int, input().split())
taste = [l+i for i in range(n)]
tasteabs = [abs(l+i) for i in range(n)]
d = tasteabs.index(min(tasteabs))
print(sum(taste) - taste[d])