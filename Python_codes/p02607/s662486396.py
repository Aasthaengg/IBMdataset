n = int(input())
li = list(map(int, input().split()))[:n]
count = 0
for i in range(0, n, 2):
    if li[i] % 2 != 0:
        count+=1
        
print(count)
