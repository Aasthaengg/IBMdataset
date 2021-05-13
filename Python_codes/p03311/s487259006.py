n = int(input())
a = [ int(x)-i-1 for i,x in enumerate(input().split()) ]
a.sort()
h = n//2
b = a[h]
s = b*h - sum(a[0:h]) + sum(a[h:n]) - b*(n-h)

print(s)