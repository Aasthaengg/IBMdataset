data = [int(i) for i in input().split(' ')]
A = data[0]
B = data[1]

count = 0
for i in range(A, B+1):
    i = str(i)
    l = len(str(i))
    l_half = l//2
    for j in range(l_half):
        if j == l_half-1:
            if i[j]==i[l-1-j]:
                count += 1
        if i[j]==i[l-1-j]:
            continue
        else:
            break
        
print(count)