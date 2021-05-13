N = int(input())
a = list(map(int,input().split()))
a.append(0)
ans = 0
count = 1
nm = a[0]
for i in range(1,N+1):
    if nm == a[i]:
        count += 1
    else:
        nm = a[i]
        ans += count//2
        count = 1

print(ans)