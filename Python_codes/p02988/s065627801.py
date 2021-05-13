n = int(input())
plist = list(map(int, input().split()))

ans = 0

for i in range(1, n-1):
    if plist[i-1] < plist[i] < plist[i+1]:
        ans += 1
    elif plist[i-1] > plist[i] > plist[i+1]:
        ans += 1

print(ans)
