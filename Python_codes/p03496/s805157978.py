N = int(input())
a = list(map(int, input().split()))

a_min, a_max = float('inf'), -float('inf')
a_min_idx, a_max_idx = -1, -1

if min(a) == max(a):
    print(0)
    exit()

ascend = True
for i in range(N - 1):
    if a[i] < a_min:
        a_min = a[i]
        a_min_idx = i + 1
    elif a_max < a[i]:
        a_max = a[i]
        a_max_idx = i + 1
    if a[i+1] < a[i]:
        ascend = False
if ascend:
    print(0)
    exit()

count = 0
message = ''
if a_min < 0 and 0 < a_max:
    if abs(a_min) < abs(a_max):
        for i in range(N):
            if a[i] < a_max:
                a[i] += a_max
                count += 1
                message += '{} {}\n'.format(a_max_idx, i + 1)
    else:
        for i in range(N):
            if a_min < a[i]:
                a[i] += a_min
                count += 1
                message += '{} {}\n'.format(a_min_idx, i + 1)

if min(a) >= 0:
    for i in range(1, N+1):
        count += 1
        message += '{} {}\n'.format(i, min(i+1, N))
else:
    for i in range(N, 1, -1):
        count += 1
        message += '{} {}\n'.format(i, max(i-1, 1))
print(count)
print(message, end='')
