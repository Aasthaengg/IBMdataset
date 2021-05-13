N = int(input())

for i in range(0,(N//4)+2,1):
    if (N-i*4)%7 == 0:
        print("Yes")
        exit()
print("No")