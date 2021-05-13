N = int(input())

flag = False
for i in range(10):
    for j in range(10):
        if N == i*j:
            flag = True
if flag:
    print("Yes")
else:
    print("No")