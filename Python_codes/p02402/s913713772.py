N = int(input())
a = list(map(int, input().split()))
max = -float('inf')
min = float('inf')
sum = 0
for i in range(N):
    
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
    sum += a[i]
    
print(min, max, sum) 