N = int(input())
A = list(map(int,input().split()))

x = 0
ans = 0
for i in A:
    if i == x:
        ans += 1
        x = 0
        continue
        
    x = i
    
print(ans)