n, m, x = map(int, input().split())
cl = []
al = []
for i in range(n):
    l = list(map(int, input().split()))
    cl.append(l[0])
    al.append(l[1:])
result = -1
for i in range(1<<n):
    price = 0
    unders = [0] * m
    for j in range(n):
        if((i>>j & 1) == 1):
            price+=cl[j]
            for k in range(m):
                unders[k] += al[j][k]
    for j in unders:
        if(j < x):
            break
    else:
        if(result == -1):
            result = price
        else:
            result= min(result, price)
                
print(result)