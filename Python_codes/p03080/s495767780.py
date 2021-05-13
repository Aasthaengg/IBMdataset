N = int(input())
s = input()

count_r = 0
count_b = 0
for i in range(N):
    if s[i] == "R":
        count_r += 1
    else:
        count_b += 1

if count_r > count_b:
    print("Yes")
else:
    print("No")