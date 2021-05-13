N = int(input())
A = []
while N>0:
    k = 0
    cnt = 0
    while cnt<N:
        k += 1
        cnt += k
    A.append(k)
    N -= k
for a in A:
    print(a)