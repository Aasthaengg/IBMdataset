h={}
for _ in range(input()):
    a,b=raw_input().split()
    if a[0]=="f":
        print "yes" if b in h else "no"
    else:
        h[b]=1