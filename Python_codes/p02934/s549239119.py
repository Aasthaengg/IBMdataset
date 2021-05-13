n= int(input())
a = list(map(int, input().split()))
sum1= 0
for i in range(n):sum1 += 1/a[i]
print(1/sum1)
