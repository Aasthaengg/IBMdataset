n,k = map(int,input().split(' '))
l = list(map(int,input().split(' ')))
count = 0

for i in l:
    if i >= k:
        count += 1
    else:
        continue

print(count)