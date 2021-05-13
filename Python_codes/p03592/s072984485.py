n, m, k = map(int, input().split())

set_ = set([])
for i in range(n+1):
    for j in range(m+1):
        set_.add(i*j + (n-i)*(m-j))
if k in set_:
    print("Yes")
else:
    print("No")