n,a,b = map(int, input().split())
x = list(map(int, input().split()))
diff = [x[i+1] - x[i] for i in range(n-1)]
ans = 0
for i in range(1,n):
    if diff[i-1] * a > b:
        ans += b
    else:
        ans += diff[i-1] * a
# print(diff)
print(ans)

