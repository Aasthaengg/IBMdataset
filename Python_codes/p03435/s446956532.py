c = [list(map(int, input().split())) for _ in range(3)]
flg = all(
    c[0][i + 1] - c[0][i] == c[1][i + 1] - c[1][i] == c[2][i + 1] - c[2][i]
    and c[i + 1][0] - c[i][0] == c[i + 1][1] - c[i][1] == c[i + 1][2] - c[i][2]
    for i in range(2)
)
print(["No", "Yes"][flg])