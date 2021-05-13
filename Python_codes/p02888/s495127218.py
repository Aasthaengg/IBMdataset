N = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        s = l[i]+l[j]
        start = j+1
        end = N
        while start != end:
            center = (start + end)//2
            if s <= l[center]:
                end = center
            else:
                start = center + 1
        ans += end-j-1
print(ans)
