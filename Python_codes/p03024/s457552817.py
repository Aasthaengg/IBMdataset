def main():
    grade = input()
    count_win = 0
    for g in grade:
        if g == "o":
            count_win += 1
    print("YES" if count_win + 15 - len(grade) >= 8 else "NO")


if __name__ == '__main__':
    main()

