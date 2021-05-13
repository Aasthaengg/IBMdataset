N = int(input())

result = [0]*(N+1)

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            f = x*x + y*y + z*z + x*y + y*z + z*x
            if f <= N:
                result[f] += 1
for i in range(N):
    print(result[i+1])