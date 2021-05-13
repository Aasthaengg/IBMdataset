nim,mike = map(int,input().split())

array = list(map(int,input().split()))

counter = 0
for i in range(40,-1,-1):
    if counter | (1 << i) > mike:
        continue
    cnt = 0
    for j in range(nim):
        if array[j] & (1 << i) == 0:
            cnt += 1
    
    if cnt > nim - cnt:
        counter = counter | (1 << i)

result = 0
for i in range(nim):
    result += counter ^ array[i]

print(result)