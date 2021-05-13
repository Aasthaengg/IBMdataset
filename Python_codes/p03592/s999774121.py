n, m, k = map(int, input().split())
l = []
for i in range(n+1):
    for j in range(m+1):
        l.append(i*m + j*n -2*i*j)

# print(l)

if k in l:
    print("Yes")
else:
    print("No")
