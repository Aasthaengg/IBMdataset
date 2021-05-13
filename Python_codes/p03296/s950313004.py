N = int(input())
a = list(map(int,input().split()))
i = 0
ans = 0
while i < N-1:
    if a[i] == a[i+1]:
        i += 2
        ans += 1
    else:
        i += 1
print(ans)