N = int(input())
max_count = 0
for i in range(1,N+1):
    count = 0
    kari = i
    while True:
        if kari % 2 == 0:
            count += 1
            kari /= 2
        else:
            break
    if count > max_count:
        max_count = count
        ans = i
if N != 1:
 print(ans)
else:
    print(1)