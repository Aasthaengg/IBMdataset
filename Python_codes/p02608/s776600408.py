N = int(input())

temp = 0
ans = [0] * 100000
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            temp = i*i + j*j + k*k + i*j + j*k + k*i
            ans[temp] += 1

for l in range(1,N+1):
    print(ans[l])

