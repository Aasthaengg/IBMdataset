A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i in range(A+1):
    for j in range(B+1):
        if(0 <= ((X-(500*i + 100*j))/50) <= C):
            count += 1
print(count)
