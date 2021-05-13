n = int(input())
l = [int(x) for x in input().split()]

cnt = 0
for i in range(n):
    if(i%2==1):
        continue
    if(l[i]%2==1):
        cnt += 1

print(cnt)