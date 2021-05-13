n = int(input())
slist = []
ans = 0
startB, endA = 0, 0
b_a = 0
for _ in range(n):
    s = list(input())
    for j in range(len(s) - 1):
        if ("".join(s[j:j + 2]) == "AB"):
            ans += 1
    startB += 1 if s[0] == "B" else 0
    endA += 1 if s[len(s) - 1] == "A" else 0
    b_a += 1 if s[0] == "B" and s[len(s) - 1] == "A" else 0

if startB == b_a and endA == b_a:
    startB -= 1

print(ans+min(max(0, startB), max(0, endA)))
