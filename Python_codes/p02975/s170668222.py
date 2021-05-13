def main():
    hats = int(input())
    number = list(map(int, input().split()))
    count = {}
    for n in number:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    answer = False
    key = list(count.keys())
    val = list(count.values())
    if len(key) == 1 and key == [0]:
        answer = True
    elif len(key) == 2 and hats % 3 == 0:
        if (key[1] == 0 and val[0] == 2 * hats // 3 and val[1] == hats // 3) or \
                (key[0] == 0 and val[1] == 2 * hats // 3 and val[0] == hats // 3):
            answer = True
    elif len(key) == 3 and hats % 3 == 0:
        if key[0] ^ key[1] ^ key[2] == 0 and val[1] == val[2] == val[0] == hats // 3:
            answer = True
    print("Yes" if answer else "No")


if __name__ == '__main__':
    main()
