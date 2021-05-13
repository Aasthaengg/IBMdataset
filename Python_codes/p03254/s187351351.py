def resolve():
    N, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dist = []

    ans = 0
    a.sort()

    for i, con in enumerate(a):
        if i == len(a)-1:
            dist.append(x - sum(dist))

        if sum(dist) + con <= x:
            dist.append(con)
        else:
            dist.append(0)

    for i in range(len(a)):
        if a[i] == dist[i]:
            ans += 1
    print(ans)
    return
resolve()