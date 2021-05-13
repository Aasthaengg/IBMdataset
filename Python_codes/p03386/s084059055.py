a,b,k = map(int,input().split())

if (b-a+1) < k:
    for i in range(a,b+1):
        print(i)
else:  
    lst1 = [i for i in range(a,a+k)]
    lst2 = [i for i in range(b-k+1,b+1)]

    lst = sorted(list(set(lst1 + lst2)))

    for i in lst:
        print(i)