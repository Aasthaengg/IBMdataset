def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    n = int(input())
    l = [list(map(int,input().split())) for i in range(n)]
    ans = 1
    count = [0]*n
    check = set()
    game = []
    for i in range(n):
        if count[i] >= n-1 or i in check:
            continue
        ind = l[i][count[i]]-1
        if ind in check:
            continue
        if l[ind].index(i+1) == count[ind]:
            check |= set([i,ind])
            game.append([i,ind])
            count[i] += 1
            count[ind] += 1
    while True:
        gamepre = game
        check = set()
        game = []
        for i,j in gamepre:
            ci = True
            cj = True
            if count[i] >= n-1 or i in check:
                ci = False
            if count[j] >= n-1 or j in check:
                cj = False
            if ci:
                ci = True
                ind = l[i][count[i]]-1
                if ind in check:
                    ci = False
                if ci and l[ind].index(i+1) == count[ind]:
                    check |= set([i,ind])
                    game.append([i,ind])
                    count[i] += 1
                    count[ind] += 1
            if cj:
                cj = True
                ind = l[j][count[j]]-1
                if ind in check:
                    cj = False
                if cj and l[ind].index(j+1) == count[ind]:
                    check |= set([j,ind])
                    game.append([j,ind])
                    count[j] += 1
                    count[ind] += 1
        if not check:
            if sum(count) != n*(n-1):
                print(-1)
                exit()
            else:
                print(ans)
                exit()
        ans += 1
if __name__ == "__main__":
    main()
