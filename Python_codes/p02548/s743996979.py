N = int(input())

count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if N - i*j >= 1:
            count += 1
        else:
            break

print(count)