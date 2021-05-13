a, b, c = map(int, input().split())
K = int(input())

for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            x = a * 2**i
            y = b * 2**j
            z = c * 2**k
            if i+j+k<=K and y > x and z > y:
                print("Yes")
                exit()

print("No")

