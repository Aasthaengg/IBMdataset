
def main():
    a = map(int, input().split())
    a_ = sorted(a)
    print(int(a_[0] * a_[1] * 0.5))


if __name__ == "__main__":
    main()
