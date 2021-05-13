a = sorted(list(map(int, input().split())))
even = []
No = []
for i in range(3):
    if a[i] % 2 == 0:
        even.append(a[i])
    else: No.append(a[i])

if len(even) == 0 or len(even) == 3:
    ans = (a[1] - a[0])//2 + a[2]-a[1]
elif len(even) == 1:
    ans = 1
    a = sorted(even+ [No[0]+1, No[1]+1])
    ans += (a[1]-a[0])//2 + a[2]-a[1]
elif len(even) == 2:
    ans = 1
    a = sorted(No + [even[0]+ 1, even[1]+1])
    ans += (a[1]-a[0])//2 + a[2]-a[1]
print(ans)