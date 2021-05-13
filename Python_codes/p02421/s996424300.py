def main():
    n = int(input())

    points = {"taro":0, "hanako":0}

    for _ in range(n):
        taro, hanako = input().split()

        if taro > hanako:
            points['taro']   += 3
        elif taro < hanako:
            points['hanako'] += 3
        else:
            points['taro']   += 1
            points['hanako'] += 1

    print(points['taro'], points['hanako'])

if __name__ == '__main__':
    main()
