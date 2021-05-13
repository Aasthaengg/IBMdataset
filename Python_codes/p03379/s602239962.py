n = int(input())
x = list(map(int, input().split()))

x_sort = sorted(x)
ans_1 = x_sort[int(n / 2)-1]
ans_2 = x_sort[int(n / 2)]

for xi in x:
    if xi <= ans_1:
        print(ans_2)
    else:
        print(ans_1)