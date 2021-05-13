line = input().split(" ")
N = int(line[0])
M = int(line[1])

count = 0
    
for i in range(1, N+1):
    for j in range(M):
        if i+j > N:
            break
        if j == M-1:
            count += 1

print(count)