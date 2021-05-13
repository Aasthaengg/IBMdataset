n = int(input())
a = [int(_) for _ in input().split()]

b = [0]*n
c = [0]*n

b[0] = a[0]
c[0] = a[0]

for i in range(1,n):
    b[i] = a[i] + b[i-1]
    c[i] = a[i] ^ c[i-1]

b.insert(0,0)
c.insert(0,0)

res = 0
right = 1

for left in range(1,n+1):
    while right < n+1 and b[right]-b[left-1] == c[right] ^ c[left-1]:
        right += 1
    res += right - left
    if left == right:
        right += 1
        
print(res)
