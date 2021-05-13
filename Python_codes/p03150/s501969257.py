s = input()
k = "keyence"
for i in range(8):
    if s.startswith(k[:i]) and s.endswith(k[i:]):
        print("YES")
        break
else:
    print("NO")