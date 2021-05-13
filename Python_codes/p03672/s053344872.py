s = list(input())

for i in range(len(s)):
    s.pop()
    if len(s) % 2 != 0:
        continue
    if s[:int(len(s)/2)] == s[int(len(s)/2):]:
        print(len(s))
        break
