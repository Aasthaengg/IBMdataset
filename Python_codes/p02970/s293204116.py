N, D = map(int, input().split())

view = 2*D + 1
ans = N // view
if (N / view) % 1 == 0:
    print(ans)
else:
    print(ans + 1)
