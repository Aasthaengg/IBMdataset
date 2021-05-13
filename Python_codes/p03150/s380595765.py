import sys
input = lambda : sys.stdin.readline().rstrip()
mod = 10**9 + 7

s = input()

if "keyence" in s:
    print("YES")
    sys.exit()

n = len(s)
m = n - 7

for i in range(n):
    s_ = s[:i] + s[i + m:]
    if s_ == "keyence":
        print("YES")
        sys.exit()

print("NO")