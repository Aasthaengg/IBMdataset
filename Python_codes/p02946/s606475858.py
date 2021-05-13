k,x = map(int,input().split())

minx,maxx = -1000000, 1000000

if minx + (k-1) > x:
    l = [i for i in range(minx,minx+x+1)]
elif maxx - (k-1) < x:
    l = [i for i in range(maxx-x,maxx+1,-1)]
else:
    l = [i for i in range(x-(k-1),x+(k-1)+1)]

print(" ".join([str(s) for s in l]))
