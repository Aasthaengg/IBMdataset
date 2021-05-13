import sys
s = input()
counts = [0] * 26

for num in s:
    counts[ord(num) - 97] += 1
    
for i in range(26):
    if counts[i] == 0:
        print(s + chr(i + 97))
        sys.exit()

d = []
for i in reversed(range(len(s))):
    for num in d:
        if s[i] < num:
            print(s[0: i] + num)
            sys.exit()
        
    d.append(s[i])
    d.sort()

print(-1)