# Written by Shagoto

n = int(input())
arr = list(map(int, input().split(" ")))
start = 0
end = 3
count = 0

while(end <= n):
    temp = arr[start:end]
    high = max(temp)
    low = min(temp)
    if(temp[1] != high and temp[1] != low):
        count += 1
    start += 1
    end += 1

print(count)