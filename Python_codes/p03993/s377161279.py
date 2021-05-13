n = int(input())
a = [0]*(n+1)
a[1:] = map(int, input().split())
ans = set()
for i in a[1:]:
    if i==a[a[i]]:
        j, k = sorted([i, a[i]])
        ans |= {(j, k)}
print(len(ans))