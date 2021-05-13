n = int(input())
a = list(map(int, input().split()))
state = None
cnt = 1
for i in range(1, n):
    if state == None:
        if a[i] > a[i-1]:
            state = 'up'
        elif a[i] < a[i-1]:
            state = 'down'
        else:
            continue
    elif state == 'up' and a[i] < a[i-1]:
        cnt += 1
        state = None
    elif state == 'down' and a[i] > a[i-1]:
        cnt += 1
        state = None
print(cnt)
