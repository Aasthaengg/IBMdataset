N, Y = map(int, input().split())
x = -1
y = -1
z = -1
for i in range(N+1):
    for j in range(N-i+1):
        k = N-i-j
        if 10000*i + 5000*j + 1000*k == Y:
            x = i
            y = j
            z = k
            break
print(x,y,z)