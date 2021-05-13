n = int(input())
a = list(map(int,input().split()))
count = 1
key = a[0]
ans = 0
if n==1:
    print(0)
else:
    for i in range(1,n):
        if key == a[i]:
            count += 1
        else:
            ans += count//2
            key = a[i]
            count = 1
ans += count//2
print(ans)
