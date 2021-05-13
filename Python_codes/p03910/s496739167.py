N = int(input())
k = 1
while (k*(k+1))//2<N:
    k += 1
if N==(k*(k+1))//2:
    for i in range(1,k+1):
        print(i)
else:
    ind = -1
    for j in range(1,k):
        tot = 0
        for i in range(1,k+1):
            if i!=j:
                tot += i
        if tot==N:
            ind = j
            break
    for i in range(1,k+1):
        if i!=ind:
            print(i)