def main():
    S = input()

    SS = set(S)
    if len(S) == len(SS):
        print('yes')
    else:
        print('no')


if __name__ == "__main__":
    main()
