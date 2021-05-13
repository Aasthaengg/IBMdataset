count = int(input())
Tpoint = 0
Hpoint = 0
for i in range(count):
    Twrite,Hwrite = map(str,input().split())
    if Twrite == Hwrite:
        Tpoint = Tpoint + 1
        Hpoint = Hpoint + 1
    elif Twrite > Hwrite:
        Tpoint = Tpoint + 3
    else:
        Hpoint = Hpoint + 3
print('{0} {1}'.format(Tpoint,Hpoint))
