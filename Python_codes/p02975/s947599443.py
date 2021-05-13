N, *A = map(int, open(0).read().split())
A_set = set(A)

if len(A_set) == 1:
    print("Yes") if sum(A) == 0 else print("No")
elif len(A_set) == 2:
    a1, a2 = sorted(A_set)
    print("Yes") if a1 == 0 and A.count(a1) * 3 == N else print("No")
elif len(A_set) == 3:
    a1, a2, a3 = list(A_set)
    if a1 ^ a2 ^ a3 == 0 and A.count(a1) == A.count(a2) == A.count(a3):
        print("Yes")
    else:
        print("No")
else:
    print("No")
