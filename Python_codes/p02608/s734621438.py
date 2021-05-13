N = int(input())
arr = [0]*(N)
lim = int(N**0.5 + 1)
for i in range(1,lim):
    for j in range(1,lim):
        for k in range(1,lim):
            num = i**2 + j**2 + k**2 + i*j + j*k + k*i - 1
            if num <= N-1:
                arr[num] += 1

print(*arr, sep='\n')

