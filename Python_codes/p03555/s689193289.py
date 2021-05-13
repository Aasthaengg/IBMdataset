def main():
    c_list = [list(input()) for _ in range(2)]
    if c_list[0][0] == c_list[1][2] and c_list[0][1] == c_list[1][1] and c_list[0][2] == c_list[1][0]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
