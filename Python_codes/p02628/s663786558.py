n, k = map(int,input().split())
li = list(map(int, input().split()))[:n]
count = 0
li.sort()
for i in range(k):
    count+=li[i]

print(count)
