a,b = map(int,input().split())
t = 0

for i in range(a,b+1):
    m = i // 1000
    n = i % 10 * 10 + i % 100 // 10
    if n == m:
        t += 1

print(t)