lis = list(map(int,input().split()))

max_num = str(max(lis))
lis.pop(lis.index(int(max_num)))

if lis[0] > lis[1]:
    result = int(max_num + str(lis[0])) + lis[1]
else:
    result = int(max_num + str(lis[1])) + lis[0]

print(result)
