S = input()
T = "keyence"

ok = False
if S.startswith(T) or S.endswith(T):
    ok = True
for i in range(1, 7):
    left = T[:i]
    right = T[i:]
    a = S.startswith(left)
    b = S.endswith(right)
    if a and b:
        ok = True
if ok:
    print("YES")
else:
    print("NO")
