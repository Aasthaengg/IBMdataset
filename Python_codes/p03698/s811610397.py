# B - Varied
def main():
    s = input()

    s_s = set(s)

    if len(s) == len(s_s):
        print('yes')
    else:
        print('no')


if __name__ ==  "__main__":
    main()