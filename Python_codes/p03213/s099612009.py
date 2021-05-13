import numpy as np
n = int(input())
ans = 0

prime = [1]*100
prime = np.array(prime)
for i in range(2,n+1):
    temp = 1
    for j in range(2,100):
        while i%j == 0:
            i //= j
            prime[j] += 1
    # print(i,prime)
p75 = prime//75
p25 = prime//25
p15 = prime//15
p5 = prime//5
p3 = prime//3
for i in range(100):
    if p75[i] >= 1:
        ans += 1
    if p25[i] >= 1:
        for j in range(i+1,100):
            if p3[j] >= 1:
                ans += 1
                # print(i,j)
    if p15[i] >= 1:
        for j in range(i+1,100):
            if p5[j] >= 1:
                ans += 1
    if p5[i] >= 1:
        for j in range(i+1,100):
            if p15[j] >= 1:
                ans += 1
            if p5[j] >= 1:
                for k in range(j+1,100):
                    if p3[k] >= 1:
                        ans += 1
                        # print(i,j,k)
            if p3[j] >= 1:
                for k in range(j+1,100):
                    if p5[k] >= 1:
                        ans += 1 
    if p3[i] >= 1:
        for j in range(i+1,100):
            if p25[j] >= 1:
                ans += 1
            if p5[j] >= 1:
                for k in range(j+1,100):
                    if p5[k] >= 1:
                        ans += 1 
# print(prime)
# print(p5)
print(ans)