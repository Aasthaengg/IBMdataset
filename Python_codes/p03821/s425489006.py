n = int(input()); a = []; b = []; x = 0
for i in range(n): A, B = map(int, input().split()); a.append(A); b.append(B)
for i in range(n-1, -1, -1): x += b[i]-(a[i]+x-1)%b[i]-1
print(x)