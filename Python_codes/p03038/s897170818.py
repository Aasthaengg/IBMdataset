N, M = map(int,input().split())
A = sorted(list(map(int, input().split())))
p = [ list(map(int, input().split())) for i in range(M) ]
p = sorted(p, reverse=True, key=lambda x: x[1])

maxv = max(A)
minv = min(A)
ans = sum(A)

if p[0][1] < minv:
    print(ans)
else:
    cnt = 0
    j = 0
    i = 0
    for x in p:
        while(i < min(j + x[0], N)):
            if x[1] > A[i]:
                ans = ans - A[i] + x[1]
                i = i+1
            else:
                break
        else:
            j = i
            if j >= N:
                break
            continue
        break
    print(ans)