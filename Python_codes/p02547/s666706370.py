n = int(input())
d = []
c = 0
ans = 'No'
for i in range(n):
    d1, d2 = [int(_) for _ in input().split()]
    if d1 == d2:
        c += 1
    else:
        c = 0
    if c == 3:
        ans = 'Yes'
print(ans)