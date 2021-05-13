n = int(input())
s = str(input())
t = str(input())
z = s + t
for i in range(n):
    if s[i:] == t[:n-i]:
        z = s + t[n-i:]
        break
print(len(z))