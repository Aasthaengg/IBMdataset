s = input()
n = len(s)

if "keyence" == s:
    print("YES")
    exit()

for i in range(n):
    for j in range(i+1, n):
        if s[:i] + s[j:] == "keyence":
            print("YES")
            exit()

print("NO")
