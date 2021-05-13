count = 0
lis = [int(x) for x in input().split()]
while lis[0] <= lis[1]:
    if lis[2]%lis[0] == 0:
        count = count+1
    lis[0] = lis[0]+1
print(count)
