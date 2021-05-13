n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(n-2):
    if p[i] <= p[i+1] <= p[i+2]:
        count += 1
    elif p[i+2] <= p[i+1] <= p[i]:
        count += 1
print(count)
