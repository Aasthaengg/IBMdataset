N=int(input())
A=int(input())
for i in range(A+1):
    for j in range(21):
        if 500*j+i==N:
            print("Yes")
            exit()
print("No")
