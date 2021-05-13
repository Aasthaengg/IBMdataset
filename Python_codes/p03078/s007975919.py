import sys,queue,math,copy,itertools,bisect,collections
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

X,Y,Z,K = LI()
A = LI()
B = LI()
C = LI()

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

h = A[0] + B[0] + C[0] +1
l = 0
while h > l+1:
    m = (h+l) // 2

    num = 0
    for a in A:
        j = len(C) - 1
        for i in B:
            while i + C[j] < m - a:
                j -= 1
                if j < 0: break
            else:
                num += j + 1
                continue
            break
    if num >= K:
        l = m
    else:
        h = m

ans = []
for a in A:
    j = len(C) - 1
    for i in B:

        while i + C[j] <= l - a:
            j -= 1
            if j < 0: break
        else:
            for k in range(j+1):
                ans.append(a+i+C[k])
            continue
        break

ans.sort(reverse=True)
for _ in range(K-len(ans)):
    ans.append(l)
print(*ans, sep='\n')

