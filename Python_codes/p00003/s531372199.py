import sys
    
n=input()
for i in range(n):
    a, b, c = sorted(map(int, raw_input().split()))
    if a*a + b*b == c*c:
        print "YES"
    else:
        print "NO"