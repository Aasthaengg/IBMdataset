n, k = map(int, input().split())

z = 0
flag = True

for i in range(1, n+1):
    for j in range(1, k+1):
        if(j+z > n):
            flag = False
            break
    if(flag == True):
        z+=1

print(z)