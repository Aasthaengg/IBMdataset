def main():
    N = input()
    cnt = 0
    for c in N:
        if c == "2": cnt += 1
    return cnt


if __name__ == '__main__':
    print(main())