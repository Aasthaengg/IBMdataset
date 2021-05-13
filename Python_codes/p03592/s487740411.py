n,m,k = map(int, input().split())

if n*m == k:
    print("Yes")
    exit()

for i in range(n):
    for j in range(m):
        if j*(n-i) + i*(m-j) == k:
            print("Yes")
            exit()
print("No")