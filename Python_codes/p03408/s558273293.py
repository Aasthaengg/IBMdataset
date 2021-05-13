def resolve():
    N = int(input())
    s = [input() for _ in range(N)]
    M = int(input())
    t = [input() for _ in range(M)]
    sdict = {k: 0 for k in set(s)}
    tdict = {k: 0 for k in set(t)}
    for w in s:
        sdict[w] += 1
    for w in t:
        tdict[w] += 1
    ks = set(s) | set(t)
    ans = 0
    for key in ks:
        ans = max(ans, sdict.get(key, 0) - tdict.get(key, 0))

    print(ans)

    return
resolve()