K = "keyence"
S = input()

for i in range(len(K) + 1):
    l, r = K[:i], K[i:]
    if S.startswith(l) and S.endswith(r):
        print("YES")
        break
else:
    print("NO")
