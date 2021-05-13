K, S = [int(x) for x in input().split()]
ans = 0
for x in range(K+1):
    for y in range(K+1):
        a = S-x-y
        if a <= K and a >= 0:
            ans +=1
print(ans)