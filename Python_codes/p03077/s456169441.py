n,*L = map(int,open(0).read().split())
min1 = min(L)
ri = 0
if n <= min1:
    print(5)
    exit()
if n%min1 == 0:
    ri = n//min1
else:
    ri = n//min1 +1
        
print(ri +4)