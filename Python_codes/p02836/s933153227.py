s = input()
n = len(s) // 2
p = n
j = -1

for i in range(n):
    if s[i] == s[j]:
        p -= 1
    j -= 1

print(p)