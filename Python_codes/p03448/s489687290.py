from itertools import product


def main():
    c500 = int(input())
    c100 = int(input())
    c50 = int(input())
    target = int(input())

    count = 0
    for n_c500, n_c100, n_c50 in product(range(c500+1), range(c100+1),  range(c50+1)):
        if (n_c500*500+n_c100*100+n_c50*50 == target): count += 1
    print(count)

if __name__ == '__main__':
    main()
