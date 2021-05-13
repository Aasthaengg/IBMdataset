n,x = map(int,input().split())
l = list(map(int,input().split()))

sum = 0
cnt = 1
for i in range(0,len(l)):
    sum += l[i]
    if sum <= x:
        cnt += 1
print(cnt)