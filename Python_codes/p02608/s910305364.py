N = int(input())
ans = [0]*(N+1)
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            n = x*x + y*y + z*z + x*y + y*z + z*x
            if n <= N:
                ans[n] += 1
print(*ans[1:], sep='\n')