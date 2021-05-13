n,t = list(map(int,input().split()))
a = list(map(int,input().split()))
max_array = [0]*(n+1)
for i in range(n-1,-1,-1):
    max_array[i] = max(max_array[i+1],a[i])
max_diff = 0
for i in range(n):
    max_diff = max(max_diff,max_array[i] - a[i])
count = 0
for i in range(n):
    count += (max_array[i] - a[i]) == max_diff
print(count)