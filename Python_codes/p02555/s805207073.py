import math


def main():
    s = int(input())
    quo = int(s/3)
    count = 0

    for i in range(1, quo+1):
        a = math.factorial((s-3*i)+(i-1))
        b = math.factorial(s-3*i)
        c = math.factorial(i-1)
        add = a//(b*c)
        count += add

    return count % (10**9+7)


if __name__ == "__main__":
    print(main())
