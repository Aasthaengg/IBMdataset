"""
D - Grid Components

２つの大きな領域を描画後、点を打っていけば良いらしい
"""

a, b = map(int, input().split())

square_n = int((max(a, b) ** 0.5) * 2 + 1)

#print(square_n)

white_p = 1
black_p = 1
white_mat = [["." for n in range(square_n)] for m in range(square_n)]
black_mat = [["#" for n in range(square_n)] for m in range(square_n)]

#print(white_mat)
#print(black_mat)

def paint(target_p, current_p, matrix, char):
    for row in range(0, square_n, 2):
        for col in range(0, square_n, 2):
            # 交互になってるので塗る
            if current_p != target_p:
                #print(row, col)
                matrix[row][col] = char
                current_p += 1
            else:
                return

paint(a, white_p, black_mat, ".")
paint(b, black_p, white_mat, "#")

print(square_n*2, square_n)
#print(white_mat)
#print(black_mat)

for row in white_mat:
    print("".join(row))
for row in reversed(black_mat):
    print("".join(row))
