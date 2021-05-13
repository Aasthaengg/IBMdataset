import math

K = int(input())
ans = 0
l = []
for i in range(K+1):
    l.append([0]*(K+1))

for i in range(1, K+1):
    for j in range(i, K+1):
        for k in range(j, K+1):
            num = math.gcd(math.gcd(i, j), k)
            if i == j:
                if j == k:
                    ans += num
                else:
                    ans += 3*num
            else:
                if j == k:
                    ans += 3*num
                else:
                    ans += 6*num

print(ans)