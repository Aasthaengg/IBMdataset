import sys
s = input()
target = "keyence"

if s == target:
    print("YES")
    sys.exit()
for i in range(len(s)):
    for j in range(i, len(s)):
        st = s[:i] + s[j:]
        if st == target:
            print("YES")
            sys.exit()

print("NO")