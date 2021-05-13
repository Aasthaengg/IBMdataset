if __name__ == '__main__':
    N, M = map(int, input().split())
    PY = []
    for i in range(1, M+1):
        p, y = map(int, input().split())
        PY.append((y, p, i))
    PY.sort()
    ANS = [""]*(M+1)
    P = [0]*(N+1)
    for y, p, i in PY:
        P[p] += 1
        ANS[i] = "{0:06d}".format(p) + "{0:06d}".format(P[p])
    
    for ans in ANS:
        if ans=="": continue
        print(ans)