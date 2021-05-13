n, k = list(map(int, input().split(' ')))

c = [k - 1] * 1000
c[0] = k
c = c[0:n]

result = 1
for i in c:
    result *= i

print(result)
    
