def main():
    s_shaped_piece, c_shaped_piece = map(int, input().split())
    answer = min(s_shaped_piece, c_shaped_piece // 2)
    c_shaped_piece -= answer * 2
    answer += c_shaped_piece // 4
    print(answer)


if __name__ == '__main__':
    main()

