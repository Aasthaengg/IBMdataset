n = int(input())
x = (-1+(1+8*n)**0.5)/2
m = int((-1+(1+8*n)**0.5)//2)
if x != m:
    print('No')
else:
    print('Yes')
    k = 2*n//m
    print(k)
    s = [[] for i in range(k)]
    add = 1
    for i in range(m):
        for j in range(i+1, k):
            s[i].append(add)
            s[j].append(add)
            add += 1
    for i in range(k):
        print(m, ' '.join([str(j) for j in s[i]]))