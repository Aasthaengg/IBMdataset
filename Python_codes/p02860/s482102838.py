n = int(input())
s = input()
c = 0
for i in range((n//2)):
    if s[i] == s[i+(n//2)]:
        c+= 1
if c*2 == n:
    print("Yes")
else:
    print("No")
