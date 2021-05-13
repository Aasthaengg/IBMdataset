n = int(input())

li = [3,5,7,11,13]
ans = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(5):
        if i%li[j]==0:
            cnt += 1
    if cnt ==3:
        ans +=1

if n>=135:
    ans += 1
if n>=189:
    ans += 1

print(ans)