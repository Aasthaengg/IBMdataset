
def main():
    num = int(input())
    data = []
    if num % 2 == 0:
        for i in range(num // 2):
            data.append([i + 1, num - i])
    else:
        for i in range((num - 1) // 2):
            data.append([i + 1, num - 1 - i])
        data.append([num])

    ans = []
    for i in range(len(data) - 1):
        for from_num in data[i]:
            for j in range(i+1, len(data)):
                for to_num in data[j]:
                    ans.append([from_num, to_num])

    print(len(ans))
    for ans_data in ans:
        print(ans_data[0], ans_data[1])


if __name__ == '__main__':
    main()