def find_operation_num(word):
    count = 1
    before = word[0]
    result = 0
    for w in word[1:] + " ":
        if before == w:
            count += 1
        else:
            before = w
            result += count // 2
            count = 1
    return result


def main():
    # 等差数列を利用する
    word = input()
    repeat = int(input())
    answer = 0
    if len(set(list(word))) == 1:
        answer = len(word) * repeat // 2
    else:
        count = [find_operation_num(word * i) for i in range(1, 3)]
        answer = count[0] + (repeat - 1) * (count[1] - count[0])
    print(answer)


if __name__ == '__main__':
    main()

