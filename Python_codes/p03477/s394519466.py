def main():
    weights = list(map(int, input().split()))
    if sum(weights[:2]) > sum(weights[2:]):
        print("Left")
    elif sum(weights[:2]) == sum(weights[2:]):
        print("Balanced")
    else:
        print("Right")


if __name__ == '__main__':
    main()