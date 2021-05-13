n = int(input())
h = list(map(int, input().split()))
MAX = 0

step = 0
for i in range(n-1):
    if h[i]-h[i+1]>=0:
        step += 1
    else:
        MAX = max(MAX, step)
        step = 0
MAX = max(MAX, step)
print(MAX)