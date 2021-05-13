n =int(input())

for i in range(100//4+1):
    for j in range(100//7+1):
        if n == i*4+j*7:
            print("Yes")
            exit()

print("No")
