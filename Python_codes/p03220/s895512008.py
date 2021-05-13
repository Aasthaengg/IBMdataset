n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))

x = 10000000
s = 0

for i in range(n):
    if abs((t * 1000 - h[i] * 6) - (a * 1000)) < x:
        s = i+1
        x = abs((t * 1000 - h[i] * 6) - (a * 1000))

print(s)
