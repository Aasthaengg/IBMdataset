import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = list(map(int,input()))
    count = 0

    S = len(N)
    flag = 0
    for i in range(S):
        temp = flag + N[-1 - i]
        if temp > 5:
            count += 10 - temp
            flag = 1
        elif temp ==5  and i !=S-1 and N[-1-i-1]>=5:
            count+=temp
            flag=1

        else:
            count += temp
            flag = 0

    print(count + flag)


if __name__ == "__main__":
    main()
