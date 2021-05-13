n = int(input())
k = int(input())
array = list(map(int,input().split()))
count = 0
for i in array:
    count += min([i,k-i])
print(count*2)