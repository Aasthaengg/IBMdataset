a, b = list(map(int, input().split()))

c = ((a**2) - (b**2)) 
d = 2*(a-b)
e = c/d

if int(e) == e:
    print(int(e))
else:
    print("IMPOSSIBLE")