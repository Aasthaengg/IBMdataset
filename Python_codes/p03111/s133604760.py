def solve(i, al, bl, cl, nu):
    if i == N:
        lal, lbl, lcl = len(al), len(bl), len(cl)
        if lal == 0 or lbl == 0 or lcl == 0:
            return
        mp = 0
        mp += 10*(len(al)-1) if len(al) > 1 else 0
        mp += 10*(len(bl)-1) if len(bl) > 1 else 0
        mp += 10*(len(cl)-1) if len(cl) > 1 else 0
        mp += abs(sum(al)-A)
        mp += abs(sum(bl)-B)
        mp += abs(sum(cl)-C)
        global min_mp
        min_mp = min(min_mp, mp)
        return
    solve(i+1, al+[L[i]], bl, cl, nu)
    solve(i+1, al, bl+[L[i]], cl, nu)
    solve(i+1, al, bl, cl+[L[i]], nu)
    solve(i+1, al, bl, cl, nu+[L[i]])


N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
min_mp = 10**10
solve(0, [], [], [], [])
print(min_mp)