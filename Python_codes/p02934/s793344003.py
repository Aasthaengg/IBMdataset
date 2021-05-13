n = int(input())
a = list(map(int, input().split()))
list = []

for i in range(n):
    list.append(1/a[i])
    
print(1/ sum(list))