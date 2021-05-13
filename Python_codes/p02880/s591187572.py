N = int(input())
flag = 0
for i in range(1,10):
    if N%i == 0:
        if N/i <= 9:
            flag = 1
            print("Yes")
            break
if flag == 0:
    print("No")