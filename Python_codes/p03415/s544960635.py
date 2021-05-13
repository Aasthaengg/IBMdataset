def main():
    grids = [""] * 3
    for i in range(3):
        grids[i] = input()
    answer = ""
    for i in range(3):
        answer = answer + grids[i][i]
    print(answer)


if __name__ == '__main__':
    main()