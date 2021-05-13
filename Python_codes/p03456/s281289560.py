a, b = input().split()
num = int(a+b)
for i in range(1,317) :
    if num == i ** 2 :
        print("Yes")
        break
else :
    print("No")
