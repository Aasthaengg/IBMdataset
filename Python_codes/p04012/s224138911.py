w = list(input())
a = list("abcdefghijklmnopqrstuvwxyz")
f = 0
for i in range(26):
    if w.count(a[i]) % 2 == 1:
        f = 1
print("Yes" if f == 0 else "No")