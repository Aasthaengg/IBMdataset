n = int(input())
a = []
ans = 0
for _ in range(n):
    a.append(int(input()))
if a[0] != 0:
    ans = -1
else:
    for i in range(n - 1):
        if (a[i+1] - a[i]) > 1:
            ans = -1
            break
        else:
            if a[i+1] == a[i]:
                if a[i+1] > 0:
                    ans += a[i+1] - 1
            if a[i+1] > 0:
                ans += 1
            if a[i+1] < a[i]:
                if a[i+1] > 1:
                    ans += a[i+1] - 1
            
print(ans)