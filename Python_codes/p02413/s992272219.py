r, c = map(int, input().split())
last_list = [0] * (c + 1)
for _ in range(r):
    n = 0
    x = input()
    sum_list = list(map(int, x.split()))
    for i in range(c):
        last_list[i] += sum_list[i]
        n += sum_list[i]
    print(x, n)

last_list[-1] = sum(last_list)
print(*last_list)