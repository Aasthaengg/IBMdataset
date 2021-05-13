import math
N = int(input())

def f(x,y,z):
    return x*x + y*y + z*z + x*y + y*z + z*x

ans = [0]*(N+1)

# upper = math.ceil(math.sqrt(N/6)) + 1
upper = int(math.sqrt(N)) + 1

for x in range(1, upper+1):
    for y in range(1, upper + 1):
        for z in range(1, upper + 1):
            v = f(x,y,z)
            if v <= N:
                ans[v] += 1
            else:
                break

for i in range(1, N+1):
    print(ans[i])