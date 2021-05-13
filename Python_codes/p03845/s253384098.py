input()
(*t,) = map(int, input().split())
sum_t = sum(t)
for _ in range(int(input())):
    p, x = map(int, input().split())
    print(sum_t - t[p - 1] + x)