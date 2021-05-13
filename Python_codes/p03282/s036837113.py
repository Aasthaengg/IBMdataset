def solve():
    S = input()
    K = int(input())
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            exit()
        elif i == K - 1:
            break
    print(1)


if __name__ == "__main__":
    solve()