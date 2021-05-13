s = list(input())
t = input()
for i in range(len(s)):
    rotate_s = s.pop()
    s.insert(0, rotate_s)
    if "".join(s) == t:
        print("Yes")
        exit()
print("No")
