n = int(input())
s = input()

num_r = 0
num_b = 0

for v in s:
    if v == "R":
        num_r += 1
    else:
        num_b += 1

if num_r > num_b:
    print("Yes")
else:
    print("No")
