n=int(input())
d=[int(x) for x in input().split()]
if n%2==1:
    print(0)
    exit()
d.sort()
print(d[n//2]-d[n//2-1])