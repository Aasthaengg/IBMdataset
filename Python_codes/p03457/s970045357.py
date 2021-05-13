N = int(input())
ex_t, ex_x, ex_y = 0, 0, 0
count = 0
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x-ex_x) + abs(y-ex_y) <= abs(t-ex_t) and t%2 == (x+y)%2:
        count += 1
    ex_t, ex_x, ex_y = t, x, y
print('Yes' if count == N else 'No')