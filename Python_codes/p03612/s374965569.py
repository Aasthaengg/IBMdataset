n = int(input())
a = list(map(int,input().split()))
b = [1 if a[i] == i+1 else 0 for i in range(n)]
ans = 0
for i in range(n-1):
    if b[i] and b[i+1]:
        b[i] = 0
        b[i+1] = 0
        ans += 1
print(ans+sum(b))