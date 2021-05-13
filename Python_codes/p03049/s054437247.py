import sys
def ii(): return int(sys.stdin.readline())

N = ii()
S = [sys.stdin.readline().rstrip() for _ in range(N)]
ans = 0
count = [0, 0, 0]
for s in S:
    ans += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        count[0] += 1
    elif s[0] == "B":
        count[1] += 1
    elif s[-1] == "A":
        count[2] += 1
if count[0]:
    ans += count[0] - 1
    if count[1]:
        ans += 1
        count[1] -= 1
    if count[2]:
        ans += 1
        count[2] -= 1
ans += min(count[1:])
print(ans)
    
