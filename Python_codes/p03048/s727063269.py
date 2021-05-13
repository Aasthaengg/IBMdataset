r, g, b, n = map(int, input().split())
count = 0
for i in range(0, n+1, r):
    rem = n-i
    for j in range(0, rem+1, g):
        if (rem-j)%b==0:
            count += 1
print(count)
