def main():
    A, B, C = map(int, input().split())
    number = sorted([A, B, C], reverse = True)
    print(int(10*number[0] + number[1] + number[2]))
if __name__ == "__main__":
    main()