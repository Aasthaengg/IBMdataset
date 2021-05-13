a = input().split()
ans = 'YES'
for i in range(len(a)-1):
    if a[i][-1] != a[i+1][0]:
        ans = 'NO'
print(ans)