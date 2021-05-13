n = int(input())
h = list(map(int, input().split()))

count = 0
count_list = []

for i in range(n-1):
    if h[i] >= h[i+1]:
        count += 1
    else:
        count_list.append(count)
        count = 0
else:
    count_list.append(count)
        
print(max(count_list))