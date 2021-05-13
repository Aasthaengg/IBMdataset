a, b, c = [int(i) for i in input().split()]
 
ans = 0
for i in range(1, c+1):
    if i%a == 0:
        ans += b
 
print(ans)