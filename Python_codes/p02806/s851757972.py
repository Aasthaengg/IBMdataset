def FallenAsleep():
    playlist = []
    timelist = []
    N = int(input())
    for _ in range(N):
        s, t = input().split()
        playlist.append(s)
        timelist.append(int(t))
    X = input()
    num = playlist.index(X)
    if num == N:
        print(0)
        return()
    else:
        print(sum(timelist[num + 1:]))
        return()



FallenAsleep()
