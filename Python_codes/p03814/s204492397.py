s = input()

rs  = s[::-1]

inds = 0
indrs = 0

for i in range(len(s)):
    if s[i] == "A":
        inds = i
        break
    
for j in range(len(rs)):
    if rs[j] == "Z":
        indrs = j
        break

indrs = len(s) - indrs

print(abs(indrs - inds))
