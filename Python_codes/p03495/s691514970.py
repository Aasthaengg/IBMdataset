n,k = map(int,input().split())
a = list(map(int,input().split()))

if(len(set(a)) <= k):
    print(0)
else:
    dic_a = {x:0 for x in set(a)}
    for i in a:
        dic_a[i] += 1
    sum = 0
    a = sorted(dic_a.values(),reverse=True)
    for i in range(k,len(a)):
        sum += a[i]
    print(sum)