N = int(input())
A = 0
B = 0
AB = 0
ans = 0
for _ in range(N):
    s = list(input())
    if s[0] == "B" and s[-1] == "A":
        AB += 1
    elif s[0] == "B":
        B += 1
    elif s[-1] == "A":
        A += 1
    for i in range(len(s) - 1):
        if s[i:i + 2] == list("AB"):
            ans += 1
if A == 0 and B == 0 and AB > 0:
    ans -= 1
print(ans + AB + min(A, B))