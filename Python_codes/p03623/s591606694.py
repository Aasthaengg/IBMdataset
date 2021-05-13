def main():
    x, a, b = map(int, input().split())
    if abs(x-a) < abs(x-b):
        return "A"
    else:
        return "B"



if __name__ == '__main__':
    print(main())