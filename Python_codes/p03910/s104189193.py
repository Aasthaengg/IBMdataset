N = int(input())
k = 1
while (k*(k+1))//2<N:
    k += 1
A = [i for i in range(1,k+1)]
if N==(k*(k+1))//2:
    for a in A:
        print(a)
else:
    m = (k*(k+1))//2-N
    for a in A:
        if a!=m:
            print(a)