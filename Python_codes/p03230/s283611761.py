from math import sqrt
n = int(input())
k = (1+sqrt(1+8*n))/2
if k.is_integer():
    print('Yes')
    k = int(k)
    ans = [set() for _ in range(k)]
    i = 1
    for j in range(k-1):
        for l in range(j+1,k):
            ans[j].add(i)
            ans[l].add(i)
            i += 1
    print(k)
    for a in ans:
        print(k-1,' '.join(map(str,a)))
else:
    print('No')
