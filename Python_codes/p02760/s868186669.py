A1 = [int(_) for _ in input().split()]
A2 = [int(_) for _ in input().split()]
A3 = [int(_) for _ in input().split()]
A_list = A1 + A2 + A3
N = int(input())
b_list = []
for _ in range(N):
    b_list.append(int(input()))

bingo_card = [False for _ in range(9)]

for b in b_list:
    for i in range(9):
        if A_list[i] == b:
            bingo_card[i] = True

flg = False

patterns = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

for pattern in patterns:
    if (
        bingo_card[pattern[0]]
        == bingo_card[pattern[1]]
        == bingo_card[pattern[2]]
        == True
    ):
        flg = True

if flg:
    print("Yes")
else:
    print("No")