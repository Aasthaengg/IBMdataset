n, y = map(int, input().split())
judge = "no value"

for i in range(n+1):
    if judge == "Found it!":
        break
    for j in range(n+1):
        z = n - i - j
        value = z * 10000 + i * 5000 + j *1000
        if value == y and z >= 0:
            print(z, i , j)
            judge = "Found it!"
            break

if judge == "no value":
    print(-1, -1, -1)
