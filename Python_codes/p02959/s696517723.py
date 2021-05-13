n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
for i in range(n):
    d = min(a[i],b[i])
    ans += d
    a[i] -= d
    b[i] -= d
    d = min(a[i+1],b[i])
    ans += d
    a[i+1] -= d
    b[i] -= d

print(ans)
