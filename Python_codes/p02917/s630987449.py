n = int(input())
b = list(map(int, input().split()))

ans = b[-1]+b[0]
for i in range(n-2):
    if b[-i-2] <= b[-i-1]:
        ans += b[-i-2]
    else:
        ans += b[-i-1]
print(ans)
