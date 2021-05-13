n = int(input())
A = list(map(int, input().split()))

sum1 = 0
for i in range(n):
    sum1 += 1/A[i]
    
sum = 1 / sum1
print(sum)