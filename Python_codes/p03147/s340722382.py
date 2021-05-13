N = int(input())
H = list(map(int, input().split()))
is_init = True
is_end = False
ans = 0
while not is_end:
    is_init = True
    for i in range(N):
        h = H[i]
        if h <= 0:
            if i == N - 1 and is_init:
                is_end = True
            H[i] -= 1
        else:
            is_init = False
            if i - 1 >= 0:
                pre = H[i - 1]
                if pre <= -1:
                    ans += 1
            else:
                if h != 0:
                    ans += 1
            H[i] -= 1
print(ans)