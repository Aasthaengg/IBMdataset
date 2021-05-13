n,k = map(int,input().split())
flag = True
count = 0
while flag:
    if k <= n:
        count += 1
        k += 1
    else:
        flag = False
print(count)