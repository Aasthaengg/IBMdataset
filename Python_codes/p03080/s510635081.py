N = int(input())
s = input()
count = 0
for c in s:
    if c == "R":
        count += 1
if count > N//2:
    print("Yes")
else:
    print("No")
