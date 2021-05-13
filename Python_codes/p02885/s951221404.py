def main():
    A, B = map(int, input().split())
    area = A - 2*B
    if area > 0:
        print(area)
    else:
        print(0)
if __name__ == "__main__":
    main()