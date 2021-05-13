N = int(input())
s = input()
count = 0
for i in s:
    if i == "R":
        count += 1
if count > N/2:
    print("Yes")
else:
    print("No")