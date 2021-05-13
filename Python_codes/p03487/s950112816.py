n = int(input())
a = list(map(int,input().split()))
a.sort()
count = 1
ans = 0
for i in range(n-1):
    if a[i+1] != a[i]:
        if count >= a[i]:
            ans += count-a[i]
        else:
            ans += count
        count = 1
    else:
        count+=1
if count >= a[-1]:
    ans += count-a[-1]
else:
    ans += count
print(ans)