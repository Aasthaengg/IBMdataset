S = input()
k = "keyence"
if S.startswith(k) or S.endswith(k):
    print("YES")
    exit()
for i in range(1, len(k)):
    if S.startswith(k[:i]) and S.endswith(k[i:]):
        print("YES")
        break
else:
    print("NO")
