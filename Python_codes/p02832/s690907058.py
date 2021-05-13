n = int(input())
a = list(map(int,input().split()))
ans = 0
count = 1

for i in range(n):
    if a[i] == count:
        count += 1

ans = n-count+1

if 1 not in a:
    ans = -1

print(ans)