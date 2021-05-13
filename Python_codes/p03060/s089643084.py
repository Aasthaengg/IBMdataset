import math


def main():
    n = int(input())
    # a, b, t = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sub = [v[i]-c[i] for i in range(n)]

    ans = 0
    for num in sub:
        if num >0:
            ans +=num

    print(ans)






if __name__ == '__main__':
    main()
