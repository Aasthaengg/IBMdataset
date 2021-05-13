n, k =map(int,input().split())
data = list(map(int,input().split()))
data = sorted(data, reverse=True)
sum = 0
for i in range(k):
    sum += data[i]
print(sum)    