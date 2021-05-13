n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n+1):
        z = n - i - j
        value = z * 10000 + i * 5000 + j *1000
        if value == y and z >= 0:
            print(z, i , j)
            break
        
    else:
        continue
    
    break

else:
    print(-1, -1, -1)