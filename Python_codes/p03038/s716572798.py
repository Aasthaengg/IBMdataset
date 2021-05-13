n, m =map(int,input().split())
A = list(map(int,input().split()))
BC = [tuple(map(int,input().split()))for i in range(m)]

A.sort()
BC.sort(key= lambda x : -x[1])


i = 0
for b, c in BC:
    for _ in range(b):
        if c <=  A[i] : break
        A[i] = c
        i += 1
        if i >= n: break
    else:continue
    break
print(sum(A))