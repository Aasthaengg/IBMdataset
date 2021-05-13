n = int(input())
a = -1
count = 0
while n-4*a > 0:
    a += 1
    if (n-4*a) % 7 == 0:
        count += 1
        break
    else:
        continue
if count == 1:
    print("Yes")
else:
    print("No")