def main():
    H = int(input())
    W = int(input())
    N = int(input())

    c_row = 0
    c_col = 0
    ans = 0

    while True:
        if N <= 0:
            print(ans)
            break
        else:
            if W - c_col <= H - c_row:
                N -=  H - c_row
                c_col += 1
                ans += 1
            else:
                N -=  W - c_col
                c_row += 1
                ans += 1

if __name__ == "__main__":
    main()