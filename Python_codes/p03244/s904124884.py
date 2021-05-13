from collections import Counter
n = int(input())
a = list(map(int,input().split()))
e = [a[k] for k in range(0,n,2)]
o = [a[k] for k in range(1,n,2)]
C = Counter(e).most_common()
D = Counter(o).most_common()
if C[0][0] != D[0][0]:
    print(n-C[0][1]-D[0][1])
else:
    if len(C) == len(D) == 1:
        print(n//2)
    elif len(C) == 1 and len(D) > 1:
        print(n-C[0][1]-D[1][1])
    elif len(D) == 1 and len(C) > 1:
        print(n-D[0][1]-C[1][1])
    else:
        print(n-max(D[0][1]+C[1][1],C[0][1]+D[1][1]))
