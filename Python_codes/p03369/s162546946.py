def main():
    s = input()
    price = 700
    for i in s:
        if i == 'o':
            price += 100
    print(price)
if __name__ == '__main__':
    main()