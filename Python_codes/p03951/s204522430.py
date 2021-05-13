from sys import stdin


def main():
    input = lambda: stdin.readline()[:-1]
    N = int(input())
    S = input()
    T = input()

    for i in range(N):
        j = 0
        for k in range(i, N):
            if S[k] != T[j]:
                break
            j += 1
        else:
            print(N * 2 - j)
            return
    print(N * 2)


main()
