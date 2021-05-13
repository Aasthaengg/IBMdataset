n = int(input())
lst = list(map(int,input().split()))
lst = sorted(lst)

ans = lst[n-1] - lst[0]
for i in range(1,n-1):
    ans += abs(lst[i])

print(ans)

for i in range(1,n-1):
    if lst[i] >= 0:
        print("%s %d" % (lst[0],lst[i]))
        lst[0] = lst[0] - lst[i]
    else:
        print("%s %d" % (lst[n-1],lst[i]))
        lst[n-1] = lst[n-1] - lst[i]
        

print("%s %d" % (lst[n-1],lst[0]))
