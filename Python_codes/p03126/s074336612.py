n,m = map(int, input().split())

lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))
    
like =[0] * 31

for i in range(n):
    for j in lis[i][1:]:
        like[j] += 1
        
cnt = 0
for k in like:
    if k == n:
        cnt += 1

print(cnt)