w, h, n = map(int, input().split())
a = [[] for _ in range(4)]
for _ in range(n):
    x, y, z = map(int, input().split())
    if z == 1 or z == 2:
        a[z-1].append(x)
    else:
        a[z-1].append(y)

x_count = 0
for i in range(w):
    flag = False

    for k in a[0]:
        if i < k:
            flag = True
            break
    if flag:
        continue
    
    for k in a[1]:
        if i >= k:
            flag = True
            break
    if flag:
        continue
    
    x_count += 1

y_count = 0
for i in range(w):
    flag = False

    for k in a[2]:
        if i < k:
            flag = True
            break
    if flag:
        continue
    
    for k in a[3]:
        if i >= k:
            flag = True
            break
    if flag:
        continue
    
    y_count += 1

print(x_count * y_count)