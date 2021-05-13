N, M = map(int, input().split())
S = input()

A = []
c = N
while c > 0:
    d = M
    while d > 0:
        if c - d >= 0 and S[c - d] == "0":
            break
        d -= 1
    else:
        print(-1)
        quit()

    c -= d
    A.append(d)

print(*reversed(A))