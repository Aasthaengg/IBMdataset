n = int(input())
h = list(map(int, input().split()))

m = 0
for i in h:
    m = max(i, m)
    if i < m-1:
        ans = 'No'
        break
else:
    ans = 'Yes'

print(ans)