d = list(map(int, input().split()))
d.sort()
s = d[0]*d[1]
print(s*(d[2]%2))
