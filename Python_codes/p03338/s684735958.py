N = int(input())
s = input()
max = 0

for i in range(1, len(s)):
    u = len(set(s[:i]).intersection(set(s[i:])))
    if u > max:
        max = u

print(max)