n = input()
b = raw_input().split()
s = list(b)

for i in range(n):
    for j in range(n - 1, i, -1):
        if b[j][1] < b[j - 1][1]:
            b[j], b[j - 1] = b[j - 1], b[j]

for i in range(n):
    mini = i
    for j in range(i, n):
        if s[j][1] < s[mini][1]:
            mini = j
    s[i], s[mini] = s[mini], s[i]

print(" ".join(b))
print("Stable")
print(" ".join(s))
print("Stable" if b == s else "Not stable")