def main():
    i = list(map(int, input().split()))
    x = i[0]
    a = i[1]
    b = i[2]

    if not (1 <= x and x <= 1000 and 1 <= a and a <= 1000 and 1 <= b and b <= 1000):
        return
    if x == a or a == b or b == x or abs(x-a) == abs(x-b):
        return

    if(abs(x-a) < abs(x-b)):
        print('A')
    else:
        print('B')

if __name__ == "__main__":
    main()