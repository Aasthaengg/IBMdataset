a,b = (int(x) for x in input().split())
c = (a*b)%2
if c == 0:
    print ('Even')
else:
    print ('Odd')