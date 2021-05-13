n = int(input())
s = input()
count = 0
for i in range(n):
    if s[i] == "R":
        count += 1
    else:
        count -= 1
if count > 0:
    print("Yes")
else:
    print("No")