
def main():
    n, m = map(int, input().split())
    if m >= 2*n:
        amari = m - 2 * n
        couple = amari // 4
        print(n + couple)
    else:
        print(m // 2)        




if __name__ == "__main__":
    main()