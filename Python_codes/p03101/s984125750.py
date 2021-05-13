H, W = map(int, input().split())
h, w = map(int, input().split())

all_cells = (H * W)
checked_as_row = (W * h)
checked_as_col = (H * w)
duplicated_check = (h * w)

# 全マス - 埋めた行 - 埋めた列 + 重複して埋めたマス
rest_cells = all_cells - checked_as_row - checked_as_col + duplicated_check

print(rest_cells)
