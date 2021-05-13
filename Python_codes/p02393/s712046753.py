lis = map(int, raw_input().split())

for i in range(len(lis)):
    j = i + 1
    for j in range(j, len(lis)):
        if lis[j] < lis[i]:
            tmp = lis[j]
            lis[j] = lis[i]
            lis[i] = tmp
print "%s %s %s" %(lis[0], lis[1],lis[2])