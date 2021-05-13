def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input())-1)

    answer = -1
    counter = 0

    i = 0
    while True:
        counter += 1
        if i == a[i]:
            answer = -1
            break
        elif a[i] == 1:
            answer = counter
            break
        elif a[i] == 0:
            answer = -1
            break
        else:
            temp = a[i]
            a[i] = 0
            i = temp

    print(answer)


if __name__ == '__main__':
    main()
