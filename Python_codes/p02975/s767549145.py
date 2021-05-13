N = int(input())
A = [int(x) for x in input().split()]

d = dict()
for i in range(N):
    d[A[i]] = d.get(A[i], 0) + 1

if len(d) > 3:
    print('No')

else:
    k = list(d.keys())
    v = list(d.values())
    
    # a1 ^ a2 ^ a3 = 0 and an: N/3
    if len(d) == 3 and k[0]^k[1]^k[2] == 0 and v[0]==v[1]==v[2]:
        print('Yes')
    
    # a1: 2N/3, 0: N/3
    elif len(d) == 2 and ((k[0] == 0 and v[1] == 2*v[0]) or (k[1] == 0 and v[0] == 2*v[1])):
        print('Yes')
    
    # 0: N
    elif len(d) == 1 and k[0] == 0:
        print('Yes')
    
    else:
        print('No')