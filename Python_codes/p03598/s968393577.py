n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(n):
    a_diff = x[i]
    b_diff = abs(k - x[i])
    
    if a_diff < b_diff:
        ans += a_diff*2
    else:
        ans += b_diff*2

print(ans)