S = input()
K = "keyence"

for i in range(len(K) + 1):
    if S.startswith(K[:i]) and S.endswith(K[i:]):
        print("YES")
        break
else:
    print("NO")
