n = input()
total = 0
for i in range(10):
    total += n.count(str(i)) * i
if total % 9 == 0:
    print("Yes")
else:
    print("No")