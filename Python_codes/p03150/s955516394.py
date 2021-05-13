s = input()
n = len(s) - 7
for i in range(7):
    if s[:i] + s[i+n:] == 'keyence':
        print("YES")
        exit()
print("NO")