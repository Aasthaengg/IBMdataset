lst = []
for _ in range(2):
    lst.append(int(input()))
if (lst[0] % 500) <= lst[1]:
    print("Yes")
else:
    print("No")