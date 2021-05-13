# 128 B

l = list(map(int, input().split()))
max = l[0]
sum = 0

for i in range(len(l)):
    sum += l[i]
    if l[i] > max:
        max = l[i]
    
print(sum - max)