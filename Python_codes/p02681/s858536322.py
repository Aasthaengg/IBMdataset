
def main():
    s = input()
    t = input()
    t_ = t[:len(t)-1]
    if s == t_:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
