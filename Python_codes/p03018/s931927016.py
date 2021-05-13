from collections import Counter

s = list(input())
chain = {}
abcs = []
kugiri = 0
countA = 0
ans = 0

for i in range(1,len(s)):
    if not((s[i] == "B" and s[i-1] == "C") or (s[i] == "B" and s[i-1] == "A") or (s[i] == "C" and s[i-1] == "B") or (s[i] == "A" and s[i-1] == "C") or (s[i] == "A" and s[i-1] == "A")):
        kugiri = i
        countA = 0
    elif s[i-1] == "A":
        countA += 1
    if s[i] == "C" and s[i-1] == "B":
        ans += countA

print(ans)
