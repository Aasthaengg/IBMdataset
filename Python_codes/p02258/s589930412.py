n = int(input())
data = [int(input()) for i in range(n)]

min_value = data.pop(0)
earn_value = -1000000000000
for d in data:
    earn_value = max(d - min_value, earn_value)
    min_value = min(d, min_value) 
print(earn_value)