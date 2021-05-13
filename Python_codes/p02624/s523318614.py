N = int(input())

sum = 0

for j in range(1,N+1):
    k = N//j
    sum += (1+k)*k*j//2
print(sum)