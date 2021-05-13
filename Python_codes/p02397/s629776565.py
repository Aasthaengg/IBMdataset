while True:
    t=[int(i) for i in input().split()]
    if t == [0,0]:
        break
    print("%d %d"%(min(t),max(t)))