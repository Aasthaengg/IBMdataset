while True:
    count=0
    n, s = tuple([int(x) for x in raw_input().split(" ")])

    if n==0 and s==0:
        break
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j==i:
                continue
            for k in range(1, n+1):
               if k==i or k==j:
                   continue
               if i+j+k==s:
                   count+=1
    
    print count / 6