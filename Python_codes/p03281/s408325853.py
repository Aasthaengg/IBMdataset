prime = [3, 5, 7, 11, 13, 17]
N = int(input())
ans = 0
for i in range(1, N+1, 2):
    a = 1; x = i
    for j in range(6):
        n = prime[j]    #; print(i, n)
        w = 0
        while x%n == 0:
            x = x//n
            w += 1 
        a *= w + 1
        if x  == 1:
            break
    if a == 8:
        ans += 1
print(ans)