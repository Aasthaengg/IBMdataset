while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    m2=(sum(s)/n)**2  
    nijou=[]
    for i in s:
        nijou.append(i**2)
    m3=sum(nijou)/len(nijou)  
    print('{:.8f}'.format((m3-m2)**0.5))
