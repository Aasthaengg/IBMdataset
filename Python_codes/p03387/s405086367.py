def resolve():
    X = list(map(int, input().split()))
    X.sort()
    
    ans = X[-1] - X[1]
    if (X[-1]-X[0]-ans) % 2 == 0:
        ans += (X[-1] - X[0]-ans) / 2
    else:
        ans += 1
        ans += (X[-1] - X[0]-ans) / 2  + 1
    print(int(ans))

    return

resolve()