n=int(input())
city={}

for i in range(1,n+1):
    c,p=input().split()
    p=int(p)

    if c in city:
        city[c].append((i,p))
    else:
        city[c]=[(i,p)]

clst=sorted(list(city.keys()))

for c in clst:
    plst=sorted(city[c],key=lambda x:x[1],reverse=True)

    for i,_ in plst:
        print(i)
