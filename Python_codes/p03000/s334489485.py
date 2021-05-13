n, x = map(int, input().split())
l = input().split()
for i in range(n):
    l[i] = int(l[i])

cnt = 1
sum = 0
for i in range(n):
    sum += l[i]
    if sum > x:
        break
    cnt += 1
    
print(cnt)
