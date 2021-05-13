n = int(input())
L = list(map(int, input().split()))
cnt = 1
state = None
i = 1
while i < n:
    if state is None:
        if L[i] > L[i - 1]:
            state = 'up'
        elif L[i] < L[i - 1]:
            state = 'down'
        i += 1
    else:
        if state == 'up':
            while L[i] >= L[i - 1]:
                i += 1
                if i >= n - 1:
                    print(cnt)
                    exit()
            cnt += 1
            i += 1
            state = None
        else:
            while L[i] <= L[i - 1]:
                i += 1
                if i >= n - 1:
                    print(cnt)
                    exit()
            cnt += 1
            i += 1
            state = None
print(cnt)