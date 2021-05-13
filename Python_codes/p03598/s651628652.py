n = int(input())
k = int(input())
lis = list(map(int, input().split()))

ans = 0
for i in range(n):
    a = lis[i]
    b = abs(k - lis[i])
    
    if a <= b:
        ans += 2*a
    else:
        ans += 2*b

print(ans)