n = list(map(int, input()))

before = n[0]
count = 1
for i in n[1:]:
    if before == i:
        count += 1
        if count==3:
            break
    else:
        before = i
        count = 1
        
if count >=3:
    print('Yes')
else:
    print('No')