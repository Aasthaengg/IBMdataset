import numpy as np
def main():
    order = [len(el) for el in list(map(str, input().rstrip().split("T")))]
    x, y = map(int, input().split())
    order_x = order[2::2]
    order_y = order[1::2]
    L_x, L_y = len(order_x), len(order_y)
    n = 10000
    dp_x = [np.zeros(2*n, dtype=np.bool) for _ in range(L_x + 1)]
    dp_y = [np.zeros(2*n, dtype=np.bool) for _ in range(L_y + 1)]
    dp_x[0][n + order[0]] = True
    dp_y[0][n] = True
    for i, d in enumerate(order_x):
        dp_x[i+1][d:] |= dp_x[i][:2*n-d]
        dp_x[i+1][:2*n-d] |= dp_x[i][d:]
    for i, d in enumerate(order_y):
        dp_y[i+1][d:] |= dp_y[i][:2*n-d]
        dp_y[i+1][:2*n-d] |= dp_y[i][d:]
    if dp_x[L_x][n + x] and dp_y[L_y][n + y]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
