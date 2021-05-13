n = int(input())
height_lists=list(map(int, input().split()))
for i in range(1,n):
    #print(i)
    #print(height_lists)
    #print()
    if height_lists[i-1] < height_lists[i]:
        height_lists[i] -=1
    else:
        pass
cp_list = height_lists.copy()
cp_list.sort()
#print(height_lists)
#print(cp_list)

if cp_list == height_lists:
    print('Yes')
else:
    print('No')