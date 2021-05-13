n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
ans = 0
for i in range(0,n):
        if i == 0:
            ans += 0
        else:
            ans += b[n-(i//2)-1]
print(ans)