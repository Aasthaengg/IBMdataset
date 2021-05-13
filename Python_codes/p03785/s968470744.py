n, c, k = map(int, input().split())
t = sorted([int(input()) for _i in range(n)])+[float('inf')]

b = 0
time = t[0]
count = 0
for i in range(n+1):
    if t[i] > time+k or count == c:
        b += 1
        time = t[i]
        count = 0
    count += 1
print(b)