N = int(input())


ans = [0]*(N+1)
i = 102
for x in range(1,i):
    for y in range(1,i):
        for z in range(1,i):
            total = (x + y + z)**2 - (x*y + y*z + x*z)
            if total <= N:
                ans[total] += 1

for i in range(1,N+1):
    print(ans[i])