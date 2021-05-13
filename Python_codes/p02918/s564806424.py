n, k = map(int, input().split())
s = list(input())
if s.count("L") == 0 or s.count("R") == 0:
    print(n-1)
else:
    if s[0] == "L":
        target = "R"
        fir = "L"
    if s[0] == "R":
        target = "L"
        fir = "R"
    cnt = 0
    mode = False
    for i in range(n):
        if s[i] != target:
            if mode:
                cnt += 1
                mode = False
                if cnt == k:
                    break
        else: # TARGET
            mode = True
            s[i] = fir
    #print(s)
    import itertools
    res = itertools.groupby(s)
    final = 0
    #print(res)
    for a,b in res:
        final += len(list(b)) -1
    print(final)

