N, Y = [int(_) for _ in input().split()]

for x in range(0, Y//10000 + 1, 1):
    for y in range(0, Y//5000 + 1, 1):
        
        z = N - x - y
        
        if z < 0:
            break
        
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            exit()
    
print("-1 -1 -1")
