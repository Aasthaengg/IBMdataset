s = list(input())


ans = 0

for i in range(len(s)+1):
    for j in range(i, len(s) + 1):
        if s[:i] + s[j:] == list("keyence"):
            ans = 1
            break
if ans:
    print("YES")
else:
    print("NO")