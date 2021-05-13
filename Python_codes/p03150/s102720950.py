s = input()
n = len(s)
for i in range(n):
    for j in range(n-i+1):
        t = s
        t = s[:j] + s[j+i:]
        if t == "keyence":
            print("YES")
            exit()
print("NO")
