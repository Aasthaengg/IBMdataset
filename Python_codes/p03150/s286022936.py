S = input()
k = "keyence"

for i in range(len(k) + 1):
    if S[:i] == k[:i] and S[-(len(k) - i):] == k[-(len(k) - i):]:
        print("YES")
        exit()

print("NO")
