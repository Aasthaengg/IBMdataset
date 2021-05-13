N = int(input())
CA = 4
DO = 7

for i in range(25):
    for j in range(15):
        Z = CA * i + DO * j
        if Z == N:
            print("Yes")

            exit()
            
print("No")