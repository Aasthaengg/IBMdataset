N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if(sum(A) < sum(B)):
    print(-1)
else:
    p = []
    m = []
    for i in range(N):
        if(B[i]-A[i] <= 0):
            p.append(A[i]-B[i])
        else:
            m.append(B[i]-A[i])
    p.sort(reverse=True)
    ans = len(m)
    idx = 0
    res = sum(m)
    while res > 0:
        if(p[idx] == 0):
            idx += 1
            continue
        res = res - p[idx]
        ans += 1
        idx += 1

    print(ans)