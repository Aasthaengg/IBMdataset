N = int(input())
S = list(input())

x = 0
ans = 0

for S in S:
    if S == "I":
        x += 1
    if S == "D":
        x -= 1
    ans = max(ans, x) 
print(ans)