# N = int(input())
H, W = [int(i) for i in input().split()]
A = [[]]
for i in range(H):
    a = [0] + [int(i) for i in input().split()]
    A.append(a)

print_list = []
for y in range(1, H+1):
    if y % 2 == 1:
        for x in range(1, W+1):
            coin_num = A[y][x]
            if coin_num % 2 == 1:
                if x < W:
                    A[y][x+1] += 1
                    A[y][x] -= 1
                    print_list.append([y, x, y, x+1])
                elif y < H:
                    A[y+1][x] += 1
                    A[y][x] -= 1
                    print_list.append([y, x, y+1, x])
    else:
        for x in range(W, 0, -1):
            coin_num = A[y][x]
            if coin_num % 2 == 1:
                if x > 1:
                    A[y][x-1] += 1
                    A[y][x] -= 1
                    print_list.append([y, x, y, x-1])
                elif y < H:
                    A[y+1][x] += 1
                    A[y][x] -= 1
                    print_list.append([y, x, y+1, x])
print(len(print_list))
for p in print_list:
    print(*p)
