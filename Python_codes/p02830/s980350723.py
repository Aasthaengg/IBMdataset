n = int(input())
s, t = (c for c in input().split())
new = []
for i in range(0, n):
    new.append(s[i])
    new.append(t[i])
print("".join(new))