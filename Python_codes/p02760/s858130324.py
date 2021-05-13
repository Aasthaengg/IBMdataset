def solve():
    card = []
    num_pos = {}
    for i in range(3):
        row = [int(num) for num in input().split()]
        card.append(row)
        for j,num in enumerate(row):
            num_pos[num] = (i,j)

    N = int(input())
    for i in range(N):
        target = int(input())
        # print(int(input()))
        if target in num_pos:
            pos_i, pos_j = num_pos[target]
            card[pos_i][pos_j] = 0

    ans = False
    for row in card:
        if not any(row):
            ans = True
    for column in range(3):
        column_flag = True
        for i in range(3):
            if card[i][column]:
                column_flag = False
        if column_flag:
            ans = True
    diagonal_flag = True
    for i in range(3):
        if card[i][i]:
            diagonal_flag = False
    if diagonal_flag:
        ans = True
    diagonal_flag = True
    for i in range(3):
        if card[2-i][i]:
            diagonal_flag = False
    if diagonal_flag:
        ans = True
    if ans:
        print("Yes")
    else:
        print("No")
    # for row in card:
    #     print(row)

if __name__ == "__main__":
    solve()