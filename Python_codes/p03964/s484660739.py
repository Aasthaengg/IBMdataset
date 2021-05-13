n = int(input())
ratio_array = [tuple(map(int, input().split())) for _ in range(n)]

t, a = 1, 1

for x, y in ratio_array:
    m = max((t+x-1)//x, (a+y-1)//y)
    t, a = m*x, m*y

print(t + a)