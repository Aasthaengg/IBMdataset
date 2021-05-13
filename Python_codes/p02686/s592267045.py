def main():
    N = int(input())
    S = [input() for _ in range(N)]
    L1 = []
    L2 = []
    for i in range(N):
        t = 0
        mint = 0
        for s in S[i]:
            if s == "(":
                t += 1
            else:
                t -= 1
            mint = min(mint, t)
        if t >= 0:
            L1.append((t, mint))
        else:
            t = 0
            mint = 0
            for j in range(len(S[i]) - 1, -1, -1):
                if S[i][j] == ")":
                    t += 1
                else:
                    t -= 1
                mint = min(mint, t)
            L2.append((t, mint))

    L1.sort(key=lambda x: x[1], reverse=True)
    L2.sort(key=lambda x: x[1], reverse=True)
    t1 = 0
    for l, m in L1:
        if t1 + m < 0:
            return False
        t1 += l
    t2 = 0
    for l, m in L2:
        if t2 + m < 0:
            return False
        t2 += l
    if t1 == t2:
        return True
    return False


if main():
    print("Yes")
else:
    print("No")
