n = int(input())
li = list(map(int,input().split()))
ans = 100000000000000000

for i in range(1,n):
    if i == 1:
        x = sum(li[:i])
        y = sum(li[i:])
    else:
        x += li[i-1]
        y -= li[i-1]
    z = abs(x-y)
    if z < ans:
        ans = z
    
print(ans)