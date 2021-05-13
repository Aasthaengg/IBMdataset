C1 = list(input())
C2 = list(input())

ok = True
for i in range(3):
    if C1[i]!=C2[2-i]:
        ok=False
print("YES" if ok else "NO")