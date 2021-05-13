def main():
    length = int(input())
    target = list(map(int, input().split()))
    max_num = max(target)
    answer = []
    for _ in range(length):
        for i in range(max_num - 1, -1, -1):
            if len(target) >= i + 1 == target[i]:
                target.pop(i)
                answer.append(i + 1)
                break
        else:
            print(-1)
            answer = []
            break
    if answer:
        for i in range(-1, -length - 1, -1):
            print(answer[i])


if __name__ == '__main__':
    main()

