import math


def trial_division(target):
    dest = int(math.sqrt(target))

    for i in range(2, dest):
        if target % i == 0:
            return trial_division(target + 2)

    else:
        return target


def main():
    x = int(input())
    if x % 2 == 0 and x != 2:
        x += 1
    ans = trial_division(x)
    print(ans)


if __name__ == '__main__':
    main()
