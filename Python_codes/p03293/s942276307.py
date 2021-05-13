s = list(input())

t = list(input())

f = 0

for i in range(len(s)):
    s.append(s[0])
    del s[0]
    if s == t:
        f = 1
        
if f == 1:
    print("Yes")
else:
    print("No")