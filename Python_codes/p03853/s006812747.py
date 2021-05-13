h, w = list(map(int, input().split()))
c_list = [list(input()) for _ in range(h)]

for i in range(len(c_list) * 2):
    for j in range(len(c_list[0])):
        print(c_list[min((i) // 2, h - 1)][j], end="")
    print()
