w = input()
A = [0] * 26

for i in w:
    A[ord(i) - 97] += 1

flag = True
for a in A:
    if a % 2 == 1:
        flag = False


if flag == False:
    print("No")
else:
    print("Yes")