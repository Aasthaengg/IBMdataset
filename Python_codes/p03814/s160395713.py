S = input().strip()
a = 10**9
z = 0
for i, s in enumerate(S):
    if s == "A":
        a = min(i, a)
    if s == "Z":
        z = max(i, z)
print(z-a+1)
