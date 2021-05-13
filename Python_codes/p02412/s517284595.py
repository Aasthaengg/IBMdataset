while True:
    e,a = map(int,input().split())
    if e ==0 and a ==0:
        break
    cnt = 0
    for i in range(1,e+1):
        for j in range(1,e+1):
            if j<=i:
                continue
            X = a - (i + j)
            if X > j and X <=e:
                cnt +=1
    print(cnt)
