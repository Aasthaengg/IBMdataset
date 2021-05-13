n = int(input())
a = [int(i) for i in input().split()]
a.append(0)
cnt = 1
ans = 0
for i in range(1,n+1):
    if a[i-1] == a[i]:
        cnt += 1
    else:
        ans += cnt//2
        cnt = 1
print(ans)