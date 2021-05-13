n = int(input())
h = list(map(int, input().split()))

res = 0
while max(h) > 0:
    first_flag = True
    for i in range(n):
        if h[i] == 0:
            first_flag = True
            continue

        if first_flag:
            res += 1
            first_flag = False
        h[i] -= 1

print(res)