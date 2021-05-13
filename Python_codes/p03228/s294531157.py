A, B, K = map(int, input().split())
c = [A, B]
for i in range(K):
    if c[i%2]%2 == 1:
        c[i%2] -= 1
    c[(i+1)%2] += c[i%2]//2
    c[i%2] //= 2
print(*c)