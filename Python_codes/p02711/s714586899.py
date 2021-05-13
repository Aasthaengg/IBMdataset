num = input()

ans = 0

for i in range(len(num)):
    if num[i] == "7":
        ans += 1

if ans == 0:
    print("No")

else:
    print("Yes")