S, W = [ int(i) for i in input().strip().split(' ')]
if W >= S:
    print('unsafe')
else:
    print('safe')