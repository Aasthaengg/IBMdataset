import sys
k = int(input()) 
ls = [[] for _ in range(10**4)] 
i = 0
ls[0] = [e for e in range(1,10)]
di = [0]*(10**4)
di[0] = 9
if k <= 9:
    print(k)
    sys.exit()
while True:
    for j in ls[i]:
        p = str(j)[-1]
        q = int(p)
        if p == "0":
            ls[i+1].append(10*j)
            ls[i+1].append(10*j+1)
        elif p == "9":
            ls[i+1].append(10*j+8)
            ls[i+1].append(10*j+9)
        else:
            ls[i+1].append(10*j+q-1)
            ls[i+1].append(10*j+q)
            ls[i+1].append(10*j+q+1)
    di[i+1] = di[i] + len(ls[i+1])
    if di[i+1] >= k:
        print(ls[i+1][k-di[i]-1])
        break
    i += 1