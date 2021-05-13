L = 10**2+10
n = int(input())
ans = [0] * n
for i in range(1, L):
    for j in range(1, L):
        for k in range(1, L):
            x = i**2+j**2+k**2+i*j+j*k+i*k
            if x <= n:
                ans[x-1] += 1
print(*ans, sep="\n")
