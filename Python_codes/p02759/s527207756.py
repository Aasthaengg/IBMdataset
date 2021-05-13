def main():
    page = int(input())
    if (page % 2) == 1:
        print(page // 2 + 1)
    else:
        print(page // 2)
main()