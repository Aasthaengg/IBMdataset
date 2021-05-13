a, b = map(str, input().split())
num = int(a+b)
flag = False
for i in range(1, 1001):
    if i*i > num:
        break
    elif i*i == num:
        print("Yes")
        flag = True
if not flag:
    print("No")