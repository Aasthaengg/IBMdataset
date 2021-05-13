n = int(input())
k = (2*n+0.25)**(1/2)+1/2
if k-int(k) == 0:
    print("Yes")
    k = int(k)
    print(k)
    bset = [[] for i in range(k)]
    now = 1
    for i in range(k-1):
        for j in range(i+1,k):
            bset[i].append(now)
            bset[j].append(now)
            now += 1
    length = len(bset[0])
    for i in bset:
        print(length," ".join(list(map(str,i))))
else:
    print("No")