a = sorted(list(map(int, input().split())))
ans = a[0]*a[1]
for i in range(3):
    if a[i]%2==0:
        ans = 0
        break
print(ans)