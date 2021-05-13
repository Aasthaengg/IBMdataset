i=1
while True:
    xy= [int(xy) for xy in input().split()]
    if xy[0]==xy[1]==0:
        break
    else:
        print('{0} {1}'.format(sorted(xy)[0],sorted(xy)[1]))
        i +=1
