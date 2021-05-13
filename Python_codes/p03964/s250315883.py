n = int(input())
ans = 0
max_t = 0
max_a = 0
for _ in range(n):
    t, a = map(int, input().split())
    x = max(max_t//t, max_a//a, 1)
    while 1:
        if max_t <= t*x and max_a <= a*x:
            max_t = t * x
            max_a = a * x
            break
        else:
            x += 1
print(max_t + max_a)