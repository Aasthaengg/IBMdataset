import numpy as np
c = [list(map(int, input().split())) for i in range(3)]
C = np.array(c)
check = np.zeros((3, 3))

for i in range(min(c[0])+1):
    check[0] = C[0] - i
    for j in range(min(c[1])+1):
        check[1] = C[1] - j
        for k in range(min(c[2])+1):
            check[2] = C[2] - k
            if list(check[0]) == list(check[1]) and list(check[0]) == list(check[2]):
                print("Yes")
                exit()

print("No")
