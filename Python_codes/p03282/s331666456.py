# coding: utf-8


def main():
    S = input()
    K = int(input())
    ans = '1'
    tmp = -1
    for i, s in enumerate(S):
        if s != '1':
            ans = s
            break
        else:
            tmp = i

    if K - 1 <= tmp:
        ans = '1'

    print(ans)

if __name__ == "__main__":
    main()
