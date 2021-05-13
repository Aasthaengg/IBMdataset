import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

ans = 0
tmp = 0
for c in S:
    if c == "I":
        tmp += 1
    elif c == "D":
        tmp -= 1
    ans = max(ans, tmp)

print(ans)