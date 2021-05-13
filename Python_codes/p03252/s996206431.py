from collections import Counter
S = Counter(list(input()))
T = Counter(list(input()))
if len(S) != len(T):
    print("No")
else:
    Sv = []
    Tv = []
    for v in S.values():
        Sv.append(v)
    for v in T.values():
        Tv.append(v)
    Svc = Counter(Sv)
    Tvc = Counter(Tv)
    if Svc == Tvc:
        print("Yes")
    else:
        print("No")