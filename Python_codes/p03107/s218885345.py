S = input()

C0 = S.count("0")
C1 = S.count("1")

ans = 2 * min(C0, C1)
print(ans)