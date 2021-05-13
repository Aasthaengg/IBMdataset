
S = input()
na = S.count("a")
nb = S.count("b")
nc = S.count("c")

n_kind = len(set(S))
nall = na+nb+nc
mx = max(na,nb,nc)
mn = min(na,nb,nc)
rest = nall - mx

if n_kind == 1:
    if len(S) == 1:
        print("YES")
        exit()
    else:
        print("NO")
        exit()
if n_kind == 2 and len(S) == 2:
    print("YES")
    exit()
if n_kind == 2 and len(S) > 2:
    print("NO")
    exit()
if n_kind == 3:
    if mx - mn >= 2:
        print("NO")
    else:
        print("YES")
