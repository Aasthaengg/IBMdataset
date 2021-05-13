h,w,k = list(map(int,input().split()))
list1 = [[str(c) for c in input()] for j in range(h)]

count1 = 0
for i in range(1<<h):
    for j in range(1<<w):
        count = 0
        for ia in range(h):
            if i&(1<<ia):continue
            for ib in range(w):
                if j&(1<<ib):continue
                if list1[ia][ib] == '#':
                    count += 1
        if count == k:
            count1 += 1


print(count1)