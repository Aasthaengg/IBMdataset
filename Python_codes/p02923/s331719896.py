n = int(input())
h = list(map(int, input().split()))

step = 0
max_num = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        step += 1
        max_num = max(step, max_num)
    else:
        step = 0
        

print(max_num)


