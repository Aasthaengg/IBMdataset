n = int(input())
A = list(map(int, input().split()))
ans = 1
p = m = 0
c = A[0]
for i in A[1:]:
    if i > c:
        p = 1
    elif i < c:
        m = 1
    if p == 1 and m == 1:
        p = m = 0
        ans += 1
    c = i
print(ans)
# maybe pills will work??