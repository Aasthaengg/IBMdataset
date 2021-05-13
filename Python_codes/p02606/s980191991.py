L, R, d = list(map(int, input().split()))

L_int = int(L/d)
R_int = int(R/d)

L_mod = L%d
R_mod = R%d


print(R_int - L_int + 1 - (L_mod!=0))