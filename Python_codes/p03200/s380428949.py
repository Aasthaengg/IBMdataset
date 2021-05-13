import sys

s = [x for x in sys.stdin.readline().rstrip()]

black = float("inf")
ans = 0

for i in range(len(s)):
    if s[i] == "B" and black > i:
        black = i
    elif s[i] == "W" and black != float("inf"):
        ans += i - black
        black += 1

print(ans)