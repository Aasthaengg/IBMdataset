print(*["{0} {1}".format(min(x[1],x[2]),x[1]+x[2]-x[0] if x[1]+x[2]-x[0]>0 else 0) for x in [[int(x) for x in input().split()]]])