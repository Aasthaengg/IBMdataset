while True:
    s=input().split()
    t=[int(l) for l in s]
    if t[0]==0:
        break
    else:
        for i in range(t[0]):
            print("#"*t[1])
        print()
    
