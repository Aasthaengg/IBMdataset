n=int(input())
d=[int(x) for x in input().split()]
d.sort()
i=n//2-1
print(d[i+1]-d[i])