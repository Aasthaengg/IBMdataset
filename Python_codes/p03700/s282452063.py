#063_D
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
x = a - b

l, r = 0, 10 ** 9
while r - l > 1:
    k = (r + l) // 2
    
    tmp = sum([max(0, -(-(h[i] - k * b) // x)) for i in range(n)])
    if tmp > k:
        l = k
    else:
        r = k
        
print(r)