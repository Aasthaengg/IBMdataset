def resolve():
    S = input()
    X, Y = list(map(int, input().split()))
    insts = []
    cnt = 1
    series = S[0]

    for i in range(1, len(S)):
        if series == S[i]:
            cnt += 1
        else:
            insts.append((series, cnt))
            cnt = 1
            series = S[i]
    insts.append((series, cnt))
    # print(insts)
    xmoves = []
    ymoves = []
    to_x = True
    for inst in insts:
        if inst[0] == "F":
            if to_x:
                xmoves.append(inst[1])
            else:
                ymoves.append(inst[1])
        else:
            if inst[1]%2 == 1:
                to_x = not to_x
    # print(xmoves)
    # print(ymoves)
    cands = set()
    cands.add(0)
    for i, x in enumerate(xmoves):
        _cands = set()
        while cands:
            xpos = cands.pop()
            _cands.add(xpos+x)
            if not (i == 0 and insts[0][0] == "F"):
                _cands.add(xpos-x)
        cands = _cands
    if X not in cands:
        print("No")
        return

    cands = set()
    cands.add(0)
    for y in ymoves:
        _cands = set()
        while cands:
            ypos = cands.pop()
            _cands.add(ypos+y)
            _cands.add(ypos-y)
        cands = _cands
    if Y not in cands:
        print("No")
        return
    
    print("Yes")

if '__main__' == __name__:
    resolve()