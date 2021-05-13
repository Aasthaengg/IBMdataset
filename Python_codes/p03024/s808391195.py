s = list(input())
counter = 0
k = len(s)
for i in range(k):
    if s[i] == "o":
        counter += 1
if counter+(15-k) >= 8:
    print("YES")
else:
    print("NO")