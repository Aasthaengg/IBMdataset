while True:
    list=[int(x) for x in input().split()]
    if any(list):
        [a,b]=sorted(list)
        print(str(a)+" "+str(b))
    else:
        break