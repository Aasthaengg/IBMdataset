n = int( input())
list = list(map(int, input().split()))
list = sorted(list)
count = 0
for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if list[j]+list[i] > list[k] and list[i] != list[j] and list[j] != list[k]:
                count += 1
print(count)