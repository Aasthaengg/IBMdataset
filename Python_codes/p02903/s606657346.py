h, w, a, b = map(int, input().split())
ans_matrix = [['0'] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if j >= a and i < b:
            ans_matrix[i][j] = '1'
        elif j < a and i >= b:
            ans_matrix[i][j] = '1'
for i in range(h):
    print(''.join(ans_matrix[i]))
