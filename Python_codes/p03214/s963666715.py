def main():
    frames = int(input())
    integer = list(map(int, input().split()))
    average = sum(integer) / frames
    answer = 0
    target = abs(average - integer[0])
    for i in range(1, frames):
        if abs(average - integer[i]) < target:
            target = abs(average - integer[i])
            answer = i
    print(answer)


if __name__ == '__main__':
    main()

