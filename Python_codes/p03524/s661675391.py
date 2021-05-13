from collections import Counter


S = input()
C = Counter(S)
vs = sorted(list(C.values()))
if len(vs) == 1:
    print("YES") if vs[0] == 1 else print("NO")
elif len(vs) == 2:
    print("YES") if vs[0] == vs[1] and vs[0] == 1 else print("NO")
else:
    print("YES") if vs[2] - 1 <= vs[0] and vs[2] - 1 <= vs[1] else print("NO")
