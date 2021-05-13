import copy


def main():
    target = input()

    num_list = []

    def function(n):
        if n == 0:
            num_list.append([(target[0], )])
        else:
            ans = []
            for i in num_list[n-1]:
                m = list(copy.copy(i))
                m.pop()
                m.append(i[-1] + target[n])
                ans.append(m)
                m = list(copy.copy(i))
                m.append(target[n])
                ans.append(m)
            ans = tuple(ans)
            num_list.append(ans)
    for x in range(len(target)):
        function(x)
    # print(num_list[-1])
    answer = 0
    for x in num_list[-1]:
        for y in x:
            answer += int(y)
    print(answer)


if __name__ == '__main__':
    main()