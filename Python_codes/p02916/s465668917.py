n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
mae = -1
for i in range(n):
    k = a[i]
    ans += b[k -1]
    if mae == k -1:
       ans += c[k -2]
    mae = k
print(ans)