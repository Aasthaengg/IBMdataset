

def main():
    a = [int(input()) for _ in range(5)]
    k = int(input())
    a_ = sorted(a)
    if abs(a_[0] - a_[4]) <= k:
        print('Yay!')
    else:
        print(':(')


if __name__ == "__main__":
    main()
