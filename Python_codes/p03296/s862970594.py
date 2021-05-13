n = int(input())
li = list(map(int,input().split()))

ans = 0
cnt = 0
temp = -1

for i in range(len(li)):
    if  temp == li[i]:
        cnt += 1
        continue
    else:
        temp = li[i]
        ans += cnt//2
        cnt = 1
else:
    ans += cnt//2
    
        
print(ans)