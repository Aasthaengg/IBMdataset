n = int(input())
t, a = map(int, input().split())
h = input().split()
for i in range(n):
    h[i] = int(h[i])

min = 100000
min_t = 0
for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < min:
        min_t = i
        min = abs(a - (t - h[i] * 0.006))
print(min_t+1)
