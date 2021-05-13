n = int(input())
A = [int(i) for i in input().split(" ")]

avg=[]
for i in range(len(A)):
    avg.append(A[i]-(i+1))
avg.sort()
b=avg[int(n/2)]

sum = 0
for j in range(len(A)):
    sum += abs(A[j]-(b+j+1))

print(sum)
