n = int(input())
d = list(map(int, input().split()))
sum = 0

for i in range(n):
    for j in range(n):
        if i > j:
            sum += d[i]*d[j]
            
print(sum)