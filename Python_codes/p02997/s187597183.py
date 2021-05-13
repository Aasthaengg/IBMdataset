N, K = [int(x) for x in input().split()]

ok = False
if K <= (N - 1)*(N - 2)//2:
    ok = True
    e = N*(N - 1)//2 - K
    edge = []
    cnt = 0
    done = False
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            edge.append([i, j])
            cnt += 1
            if cnt == e:
                done = True
                break
        if done == True:
            break

if ok == True:
    print(e)
    for x in edge:
        print(x[0], end=' ')
        print(x[1])
else:
    print(-1)