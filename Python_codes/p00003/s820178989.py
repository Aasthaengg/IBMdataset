n = int(raw_input())
for k in range(n):
    [a,b,c] = map(int,raw_input().split())
    a,b,c = sorted([a,b,c])
    if a**2 + b**2 == c**2:
        print "YES"
    else:
        print "NO"