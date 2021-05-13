s = list(input())
t = list(input())
count = 0
if s == t:
    print("Yes")
    exit()
for i in range(len(s)):
    s.append(s.pop(0))
    if s == t:
        print("Yes")
        count += 1
        break
if count == 0:
    print("No")