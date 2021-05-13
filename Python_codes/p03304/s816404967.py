n,m,d=[int(x) for x in input().split()]

if d==0:
    print("{:.07f}".format((m-1)*1/n))
else:
    print("{:.07f}".format((m-1)*2*(n-d)/n**2))