n = int(input())
 
ans = 0
for i in range(n):
    l = input().split()
    if l[1] == "BTC":
        ans += float(l[0])*380000
    else:
        ans += int(l[0])

print(ans)