n, t = map(int, input().split())
tl = list(map(int, input().split()))

time = 0
for i in range(1, n):
    if tl[i] - tl[i-1] > t:
        time += t
    else:
        time += tl[i] - tl[i-1]

print(time + t)