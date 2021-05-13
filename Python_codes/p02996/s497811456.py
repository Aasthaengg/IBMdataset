def main():
    point = 0
    ab = []
    for i in range(int(input())):
        t = list(map(int, input().split()))
        ab.append(t)
    ab.sort(key=lambda x: x[1])
    for i in range(len(ab)):
        point += ab[i][0]
        # print(point, ab[i])
        if point > ab[i][1]:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()
