n = int(input())
cake = 4
donut = 7

for i in range(25):
    for j in range(25):
        if i*cake+j*donut==n:
            print("Yes")
            exit()

print("No")

