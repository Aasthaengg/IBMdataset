from collections import deque
s = deque(input())
t = deque(input())
for i in range(len(s)):
    if s == t:
        print("Yes")
        exit()
    s.append(s[0])
    s.remove(s[0])
print("No")