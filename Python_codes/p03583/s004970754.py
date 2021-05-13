from itertools import product
def main():
    n = int(input())
    for x, y in product(range(1, 3501), repeat = 2):
        if 4 * x * y - n * (x + y) != 0:
            z = n * x * y / (4 * x * y - n * (x + y))
        else:
            continue
        if z.is_integer() and z > 0:
            print(x, y, int(z))
            break

if __name__ == '__main__':
    main()
