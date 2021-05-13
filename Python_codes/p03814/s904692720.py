s = list(input())

for i in range(len(s)):
    if s[i] == "A":
        A = i
        break
for i in range(len(s)):
    if s[i] == "Z" and i > A:
        B = i

    
print(B - A + 1)