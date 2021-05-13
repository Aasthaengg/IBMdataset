
def main():
    n = input()
    cnt = 0

    if n[0] == n[1]:
        cnt += 1
    else:
        cnt = 0

    for i in range(2, 4):
        if n[i-1] == n[i]:
            cnt += 1
        else:
            cnt -= 1
        if cnt >= 2:
            print('Yes')
            break
    if cnt < 2:
        print('No')


if __name__ == "__main__":
    main()
