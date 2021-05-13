n = int(input())
a = [int(i) for i in input().split()] 
a.sort()
m = a[0]
M = a[n-1]
s = sum(a)
print("{} {} {}".format(m,M,s))