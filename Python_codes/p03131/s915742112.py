K,a,b = map(int,input().split())
count = 1
if (b-a) <= 2:
    count += K
else:
    K -= (a-1)
    count += (a-1)
    if K >= 2:
        count += K//2 * (b-a)
        if K % 2 ==1:
            count += 1
    else:
        count += 1
print(count)
